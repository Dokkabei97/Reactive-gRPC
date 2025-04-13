```shell
# configsvr01 컨테이너에 접속
docker exec -it configsvr01 mongosh --port 27017

# Mongo Shell 내부에서 실행
rs.initiate( {
   _id : "csrs",
   configsvr: true,
   members: [
      { _id : 0, host : "configsvr01:27017" },
      { _id : 1, host : "configsvr02:27017" },
      { _id : 2, host : "configsvr03:27017" }
   ]
})

# 확인 (출력에서 "ok": 1 확인) 후 exit 입력하여 쉘 종료
exit
```

```shell
# shard01a 컨테이너에 접속
docker exec -it shard01a mongosh --port 27017

# Mongo Shell 내부에서 실행
rs.initiate( {
   _id : "shard01rs",
   members: [ { _id : 0, host : "shard01a:27017" } ]
   # 만약 shard01b, shard01c 등 멤버를 추가했다면 members 배열에 추가해야 함
   # 예: members: [ { _id : 0, host : "shard01a:27017" }, { _id : 1, host : "shard01b:27017" }, ... ]
})

# 확인 후 exit
exit
```

```shell
# shard02a 컨테이너에 접속
docker exec -it shard02a mongosh --port 27017

# Mongo Shell 내부에서 실행
rs.initiate( {
   _id : "shard02rs",
   members: [ { _id : 0, host : "shard02a:27017" } ]
   # 멤버 추가 시 위와 동일하게 설정
})

# 확인 후 exit
exit
```

```shell
# mongos01 컨테이너에 접속 (포트는 외부 연결된 27017 또는 내부 27017 사용)
docker exec -it mongos01 mongosh --port 27017

# Mongo Shell 내부에서 실행
sh.addShard( "shard01rs/shard01a:27017" )
# 만약 shard01 레플리카셋에 멤버가 여러 개라면 대표 멤버 하나만 적어도 됨 (예: "shard01rs/shard01a:27017,shard01b:27017")

sh.addShard( "shard02rs/shard02a:27017" )
# shard02도 동일하게 설정

# 확인 (sh.status() 명령어로 추가된 샤드 확인)
sh.status()

# 확인 후 exit
exit
```