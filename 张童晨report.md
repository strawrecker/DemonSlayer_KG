## 可视化和知识问答

### 将知识图谱导入neo4j
使用docker安装neo4j
```sh
docker pull neo4j:4.4.12
```
运行容器并建立映射，设置用户名和密码
```sh
sudo docker run -d --name neo4j-4.4.12-container \
-p 7474:7474 -p 7687:7687 \
-v /home/touch/neo4j4.4.12/data:/data \
-v /home/touch/neo4j4.4.12/logs:/logs \
-v /home/touch/neo4j4.4.12/conf/:/var/lib/neo4j/conf \
-v /home/touch/neo4j4.4.12/import/:/var/lib/neo4j/import \
-v /home/touch/neo4j4.4.12/plugins/:/var/lib/neo4j/plugins \
--env NEO4J_AUTH=neo4j/123456 neo4j:4.4.12
```
使用neo4j库编写python脚本将获得的数据导入到neo4j数据库中
```sh
python ./src/create_graph.py

```

### 知识图谱可视化与查询
导入了neo4j数据库之后，可以使用网页连接设置的端口进行数据库操作，如显示所有节点
```neo4j
MATCH (n) RETURN (n)
```
结果如下
<!-- TODO graph -->

### 知识问答
使用上面建立的知识图谱，可以进行知识问答，如询问：“性别为男性的有谁？”提取出关键词“性别”和“男性”，作为输入即可获得答案，如下
```python
result = session.execute_read(relation_name_y_query_name_x, relation="性别", name_y="男")
for x in result:
    print(x)
```
结果如下
