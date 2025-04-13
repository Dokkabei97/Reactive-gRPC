#!/bin/bash

# 서버가 시작할 때까지 대기
sleep 30

# Config Server 복제셋 초기화
mongo --host config-server-1:27017 <<EOF
rs.initiate(
  {
    _id: "configReplSet",
    configsvr: true,
    members: [
      { _id : 0, host : "config-server-1:27017" },
      { _id : 1, host : "config-server-2:27017" },
      { _id : 2, host : "config-server-3:27017" }
    ]
  }
)
EOF

# Shard 1 복제셋 초기화
mongo --host shard1-server-1:27017 <<EOF
rs.initiate(
  {
    _id : "shard1ReplSet",
    members: [
      { _id : 0, host : "shard1-server-1:27017" },
      { _id : 1, host : "shard1-server-2:27017" },
      { _id : 2, host : "shard1-server-3:27017" }
    ]
  }
)
EOF

# Shard 2 복제셋 초기화
mongo --host shard2-server-1:27017 <<EOF
rs.initiate(
  {
    _id : "shard2ReplSet",
    members: [
      { _id : 0, host : "shard2-server-1:27017" },
      { _id : 1, host : "shard2-server-2:27017" },
      { _id : 2, host : "shard2-server-3:27017" }
    ]
  }
)
EOF

# 복제셋 초기화 대기
sleep 60

# 라우터에 샤드 추가
mongo --host mongos-router:27017 <<EOF
sh.addShard("shard1ReplSet/shard1-server-1:27017,shard1-server-2:27017,shard1-server-3:27017")
sh.addShard("shard2ReplSet/shard2-server-1:27017,shard2-server-2:27017,shard2-server-3:27017")
EOF

echo "MongoDB 샤딩 클러스터 설정 완료!"