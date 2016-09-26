king_count = queen_count = 1
rooks_count = bishops_count = knights_count = 2
pawns_count = 8

king, queen, rooks, bishops, knights, pawns = map(int, input().split())
print(king_count - king,
      queen_count - queen,
      rooks_count - rooks,
      bishops_count - bishops,
      knights_count - knights,
      pawns_count - pawns)
