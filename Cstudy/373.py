import matplotlib.pyplot as plt
import networkx as nx

# 1. IPE 파일에서 추출한 정확한 좌표 (Matrix 변환 적용됨)
# [참고] IPE 파일 내부 데이터 분석 결과:
# 6: (80, 240)
# 3: (544, 304)
# 7: (176, 608)
# 1: (332, 392)
# 2: (196, 436)
# 5: (232, 484)
# 8: (244, 388)
# 9: (336, 328)
# 4: (164+12, 316-12) = (176, 304)  <- Matrix 변환 적용
# p: (256-44, 368+20) = (212, 388)  <- Matrix 변환 적용

coords = {
    6: (80, 240),
    3: (544, 304),
    7: (176, 608),
    1: (332, 392),
    2: (196, 436),
    5: (232, 484),
    8: (244, 388),
    9: (336, 328),
    4: (176, 304),
    'p': (212, 388)
}

# 2. 단계별 삼각형 데이터 (알고리즘 로직 동일)
t0_tris = [
    (1,3,9), (1,3,7), (1,5,7), (1,5,8), (1,8,9), 
    (2,4,6), (2,4,8), (2,5,8), (2,5,7), (2,6,7), 
    (3,6,9), (4,6,9), (4,8,9)
]

t1_tris = [
    (3,7,9), (7,8,9), (5,7,8),  # From removing 1
    (4,6,7), (4,5,7), (4,5,8),  # From removing 2
    (3,6,9), (4,6,9), (4,8,9)   # Persisting
]

t2_tris = [
    (6,7,9), (7,8,9), (5,7,8),  # From removing 4 (Ear 6->679)
    (3,6,9), (3,7,9)            # Persisting
]

t3_tris = [
    (6,7,8), # From removing 5
    (6,8,9), (3,7,9), (3,6,9) # Persisting
]

t4_tris = [
    (6,7,9), # From removing 8
    (3,7,9), (3,6,9)
]

t5_tris = [
    (3,6,7) # Final (From removing 9)
]

stages = [t0_tris, t1_tris, t2_tris, t3_tris, t4_tris, t5_tris]
titles = ["T0 (Initial)", "T1 (Remove 1, 2)", "T2 (Remove 4)", "T3 (Remove 5)", "T4 (Remove 8)", "T5 (Remove 9) -> Final"]

# --- Part A: 그림 그리기 ---
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
axes = axes.flatten()

for i, tris in enumerate(stages):
    ax = axes[i]
    ax.set_title(titles[i], fontsize=12, fontweight='bold')
    ax.set_aspect('equal')
    ax.axis('off')
    
    # 삼각형 그리기
    for tri in tris:
        pts = [coords[v] for v in tri]
        tri_x = [p[0] for p in pts] + [pts[0][0]]
        tri_y = [p[1] for p in pts] + [pts[0][1]]
        
        ax.fill(tri_x, tri_y, edgecolor='black', facecolor='azure', alpha=0.5)
        
        # 라벨 표시
        cx = sum(p[0] for p in pts)/3
        cy = sum(p[1] for p in pts)/3
        label = "".join(str(v) for v in sorted(tri))
        
        # T0에서 점 p가 포함된 248 삼각형 강조
        if i==0 and label=='248': 
            ax.text(cx, cy, label, color='red', fontweight='bold', fontsize=9)
        else: 
            ax.text(cx, cy, label, color='blue', fontsize=8, ha='center', va='center')

    # 점 그리기
    active_verts = set([v for tri in tris for v in tri])
    for v, pos in coords.items():
        if v == 'p':
            ax.plot(pos[0], pos[1], 'r*', markersize=10)
            ax.text(pos[0], pos[1]-15, 'p', color='red', fontsize=12, ha='center')
        elif v in active_verts:
            ax.plot(pos[0], pos[1], 'ko', markersize=4)
            ax.text(pos[0]+10, pos[1], str(v), fontsize=10)

plt.tight_layout()
plt.show()

# --- Part B & C: DAG 시각화 ---
def draw_dag():
    G = nx.DiGraph()
    
    # 노드 및 계층 설정
    G.add_node('367', layer=5) # Root
    
    edges = [
        ('367', '679'), ('367', '369'), ('367', '379'), # T5->T4
        ('679', '678'), ('679', '689'),                 # T4->T3 (Remove 8)
        ('678', '578'), ('678', '467'),                 # T3->T2 (Remove 5)
        ('578', '458'), ('578', '457'),                 # T2->T1 (Remove 4)
        ('458', '248'), ('458', '258'), ('458', '489'), # T1->T0 (Remove 1,2)
        ('457', '257'), ('457', '267'),
        ('467', '246'), ('467', '267'),
        ('379', '139'), ('379', '137'),
        ('789', '189'), ('789', '489'),
        ('578', '158'), ('578', '157')
    ]
    
    # 점 P의 탐색 경로 (정답)
    p_path = ['367', '679', '678', '578', '458', '248']
    
    G.add_edges_from(edges)
    pos = nx.multipartite_layout(G, subset_key="layer", align='horizontal')
    
    plt.figure(figsize=(10, 8))
    
    # 노드 색상 설정
    colors = ['#ff9999' if n in p_path else 'lightblue' for n in G.nodes]
    
    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=1500, font_size=9, font_weight='bold')
    
    # 경로 강조
    path_edges = list(zip(p_path, p_path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
    
    plt.title("Problem 2(b) DAG & (c) Search Path (Red)", fontsize=15)
    plt.show()

draw_dag()