# -*- coding: utf-8 -*-

# Description: implement two routing algorithms (link-state routing and distance-vector routing) via Python
#
# Input: Shanghai Metro Map （上海地铁交通图）and arbitrary two stations (任意两个地铁站名：例如张江高科站到肇嘉浜路站)
#  
# Output: the least delay path (最短时间) or the least switching times with delay as low as possible (最短换乘次数的前提下总时间尽可能的少). 


class station(object):
  """docstring for station"""
  def __init__(self, name, line):
  	self.name = name
  	self.line = line

# Link-state routing -- Dijkstra's algorithm
def Dijkstra(S,path_map):
  # S is the set of all switches in network
  # math_map is the map of shortest path we want to find
  for u in S:
    N = [u]
    while len(N)<len(S):
      #find w not in N such that D(w,u) is a minimum
      d_min = float('inf')
      w = u
      for v in S:
        if v not in N and path_map[u][v][0]<d_min:
            w = v
            d_min = path_map[u][v][0]
      if w==u:
        print "ERROR: switch not connected to any other nodes"
      #add w to N
      N.append(w)

      #update D(v,u) for each neighbor v of w and not in N:
      #D(v,u) = min( D(v),D(w)+c(w,v) )
      for v in S:
        if v not in N and path_map[w][v][1]==v:
          if path_map[u][v][0] > path_map[u][w][0]+path_map[w][v][0]:
            path_map[u][v] = (path_map[u][w][0]+path_map[w][v][0], w)
  return path_map


# Distance-vector routing -- Bellman-Ford algorithm
def BellmanFord(S,path_map):
  for u in S:
    #Step1: Initialization
    D = [0] * (max(S)+1)
    for v in S:
      if u != v:
        D[u] = float('inf') 
      else:
        D[u] = 0
    #Step2: Calculate shortest path
    for v in S:
      for w in S:
        if path_map[v][w][0] is not None:
          if D[v]+path_map[v][w][0] < D[w]:
            D[w] = D[v]+path_map[v][w][0]
            path_map[u][w] = (D[w],v)
  return path_map



# The metro map
S_num = 373
S = []
path_map = [[(float('inf'),None) for j in range(S_num)] for i in range(S_num)]
for i in range(S_num):
  path_map[i][i] = (0,i)



# line 1 -- 28 stations (0-27)
line1 = ["莘庄","外环路","莲花路","锦江乐园","上海南站","漕宝路","上海体育馆","徐家汇","衡山路","常熟路","陕西南路","黄婆南路","人民广场","新闸路","汉中路","上海火车站","中山北路","延长路","上海马戏城","汶水路","彭浦新村","共康路","通河新村","呼兰路","共富新村","宝安公路","友谊西路","富锦路"]
delay1 = [2,2,3,3,3,2,3,2,2,2,2,3,2,2,1,3,2,2,3,3,2,3,2,3,3,2,2]
for i in range(len(line1)):
  S.append(station(line1[i],1))
for i in range(len(delay1)):
  path_map[i][i+1] = (delay1[i],None)
  path_map[i+1][i] = (delay1[i],None)
n = len(line1)


# line 2 -- 30 stations (28-57)
line2 = ["浦东国际机场","海天三路","远东大道","凌空路","川沙","华夏东路","创新中路","唐镇","广兰路","金科路","张江高科","龙阳路","世纪公园","上海科技馆","世纪大道","东昌路","陆家嘴","南京东路","人民广场","南京西路","静安寺","江苏路","中山公园","娄山关路","咸宁路","北新泾","淞虹路","虹桥2号航站楼","虹桥火车站","徐泾东"]
delay2 = [3,7,5,3,5,3,3,4,3,2,4,1,3,3,2,2,3,3,2,2,3,3,2,3,2,3,2,2,2]
for i in range(len(line2)):
  S.append(station(line2[i],2))
for i in range(len(delay2)):
  path_map[n+i][n+i+1] = (delay2[i],None)
  path_map[n+i+1][n+i] = (delay2[i],None)
n = n+len(line2)


# line 3 -- 29 stations (58-86)
line3 = ["上海南站","石龙路","龙漕路","漕溪路","宜山路","虹桥路","延安西路","中山公园","金沙江路","曹杨路","镇坪路","中潭路","上海火车站","宝山路","东宝兴路","虹口足球场","赤峰路","大柏树","江湾镇","殷高西路","长江南路","淞发路","张华浜","淞浜路","水产路","宝杨路","友谊路","铁力路","江杨北路"]
delay3 = [2,2,2,3,2,2,2,3,2,2,3,2,4,2,2,3,2,2,3,3,3,2,2,2,3,2,3,2]
for i in range(len(line3)):
  S.append(station(line3[i],3))
for i in range(len(delay3)):
  path_map[n+i][n+i+1] = (delay3[i],None)
  path_map[n+i+1][n+i] = (delay3[i],None)
n = n+len(line3)


# line 4 -- 26 stations (87-112)
line4 = ["宜山路","上海体育馆","上海体育场","东安路","大木桥路","鲁班路","西藏南路","南浦大桥","塘桥","蓝村路","浦电路","世纪大道","浦东大道","杨树浦路","大连路","临平路","海伦路","宝山路","上海火车站","中潭路","镇坪路","曹杨路","金沙江路","中山公园","延安西路","虹桥路"]
delay4 = [2,2,2,1,2,3,2,3,2,2,2,3,2,2,2,2,3,3,3,2,3,1,3,2,2]
for i in range(len(line4)):
  S.append(station(line4[i],3))
for i in range(len(delay4)):
  path_map[n+i][n+i+1] = (delay4[i],None)
  path_map[n+i+1][n+i] = (delay4[i],None)
n = n+len(line4)


# line 5 -- 11 stations (113-123)
line5 = ["莘庄","春申路","银都路","颛桥","北桥","剑川路","东川路","金平路","华宁路","文井路","闵行开发区"]
delay5 = [2,2,4,3,3,2,3,2,3,2]
for i in range(len(line5)):
  S.append(station(line5[i],5))
for i in range(len(delay5)):
  path_map[n+i][n+i+1] = (delay5[i],None)
  path_map[n+i+1][n+i] = (delay5[i],None)
n = n+len(line5)


# line 6 -- 28 stations (124-151)
line6 = ["港城路","外高桥保税区北","航津路","外高桥保护区南","洲海路","五洲大道","东靖路","巨峰路","五莲路","博兴路","金桥路","云山路","德平路","北洋泾路","民生路","源深体育中心","世纪大道","浦电路","蓝村路","上海儿童医学中心","临沂新村","高科西路","东明路","高青路","华夏西路","上南路","灵岩南路","东方体育中心"]
delay6 = [3,2,3,3,2,2,3,2,2,2,3,2,3,2,2,2,3,2,3,3,2,3,2,3,2,2,2]
for i in range(len(line6)):
  S.append(station(line6[i],6))
for i in range(len(delay6)):
  path_map[n+i][n+i+1] = (delay6[i],None)
  path_map[n+i+1][n+i] = (delay6[i],None)
n = n+len(line6)


# line 7 -- 33 stations (152-184)
line7 = ["花木路","龙阳路","芳华路","锦绣路","杨高南路","高科西路","云台路","耀华路","长清路","后滩","龙华中路","东安路","肇嘉浜路","常熟路","静安寺","昌平路","长寿路","镇坪路","岚皋路","新村路","大华三路","行知路","大场镇","场中路","上大路","南陈路","上海大学","祁华路","顾村公园","刘行","潘广路","罗南新村","美兰湖"]
delay7 = [3,2,3,2,3,2,2,2,2,3,2,2,3,2,3,2,2,3,2,2,2,2,3,2,2,3,3,3,3,2,4,2]
for i in range(len(line7)):
  S.append(station(line7[i],7))
for i in range(len(delay7)):
  path_map[n+i][n+i+1] = (delay7[i],None)
  path_map[n+i+1][n+i] = (delay7[i],None)
n = n+len(line7)


# line 8 -- 30 stations (185-214)
line8 = ["沈杜公路","联航路","江月路","浦江路","芦恒路","凌兆新村","东方体育中心","杨思","成山路","耀华路","中华艺术宫","西藏南路","陆家浜路","老西门","大世界","人民广场","曲阜路","中兴路","西藏北路","虹口足球场","曲阳路","四平路","鞍山新村","江浦路","黄兴路","延吉中路","黄兴公园","翔殷路","嫩江路","市光路"]
delay8 = [2,2,2,4,3,3,3,2,2,2,2,3,2,2,1,3,2,2,3,2,2,2,2,2,3,2,2,2,1]
for i in range(len(line8)):
  S.append(station(line8[i],8))
for i in range(len(delay8)):
  path_map[n+i][n+i+1] = (delay8[i],None)
  path_map[n+i+1][n+i] = (delay8[i],None)
n = n+len(line8)


# line 9 -- 26 stations (215-240)
line9 = ["杨高中路","世纪大道","商城路","小南门","陆家浜路","马当路","打浦桥","嘉善路","肇嘉浜路","徐家汇","宜山路","桂林路","漕河泾开发区","合川路","星中路","七宝","中春路","九亭","泗泾","佘山","洞泾","松江大学城","松江新城","松江体育中心","醉白池","松江南站"]
delay9 = [3,3,3,3,2,3,2,2,2,4,3,3,3,3,3,2,4,6,5,3,4,4,3,3,3]
for i in range(len(line9)):
  S.append(station(line9[i],9))
for i in range(len(delay9)):
  path_map[n+i][n+i+1] = (delay9[i],None)
  path_map[n+i+1][n+i] = (delay9[i],None)
n = n+len(line9)


# line 10 -- 31 stations (241-271)
line10 = ["新江湾城","殷高东路","三门路","江湾体育场","五角场","国权路","同济大学","四平路","邮电新村","海伦路","四川北路","天潼路","南京东路","豫园","老西门","新天地","陕西南路","上海图书馆","交通大学","虹桥路","松园路","伊犁路","水城路","龙溪路","上海动物园","虹桥1号航站楼","虹桥2号航站楼","虹桥火车站","龙柏新村","紫藤路","航中路"]
delay10 = [2,1,3,1,2,2,2,2,2,2,2,2,2,3,2,2,3,2,2,3,1,2,3,2,3,3,1]
for i in range(len(line10)):
  S.append(station(line10[i],10))
for i in range(26):
  path_map[n+i][n+i+1] = (delay10[i],None)
  path_map[n+i+1][n+i] = (delay10[i],None)
path_map[n+23][n+28] = (3,None)
path_map[n+28][n+23] = (3,None)
path_map[n+28][n+29] = (2,None)
path_map[n+29][n+28] = (2,None)
path_map[n+29][n+30] = (3,None)
path_map[n+30][n+29] = (3,None)
n = n+len(line10)


# line 11 -- 37 stations (272-308)
line11 = ["康新公路","秀沿路","罗山路","御桥","浦三路","三林东","三林","东方体育中心","龙耀路","云锦路","龙华","上海游泳馆","徐家汇","交通大学","江苏路","隆德路","曹杨路","枫桥路","真如","上海西站","李子园","祁连山路","武威路","桃浦新村","南翔","马陆","嘉定新城","白银路","嘉定西","嘉定北","上海赛车场","昌吉东路","上海汽车城","安亭","兆丰路","光明路","花桥"]
# 康新公路-嘉定新城-嘉定北
delay11 = [3,3,3,6,2,2,5,3,2,2,3,3,3,3,3,2,2,2,3,2,3,2,2,4,6,3,3,4,2]
for i in range(len(line11)):
  S.append(station(line11[i],11))
for i in range(len(delay11)):
  path_map[n+i][n+i+1] = (delay11[i],None)
  path_map[n+i+1][n+i] = (delay11[i],None)
# 嘉定新城-上海赛车场
path_map[n+26][n+30] = (4,None)
path_map[n+30][n+26] = (4,None)
# 上海赛车场-花桥
delay11_1 = [6,3,3,2,3,2]
for i in range(6):
  path_map[n+30+i][n+30+i+1] = (delay11_1[i],None)
  path_map[n+30+i+1][n+30+i] = (delay11_1[i],None)
n = n+len(line11)


# line 12 -- 32 stations (309-340)
line12 = ["金海路","申江路","金京路","杨高北路","巨峰路","东陆路","复兴岛","爱国路","隆昌路","宁国路","江浦公园","大连路","提篮桥","国际客运中心","天潼路","曲阜路","汉中路","南京西路","陕西南路","嘉善路","大木桥路","龙华中路","龙华","龙漕路","漕宝路","桂林公园","虹漕路","虹梅路","东兰路","顾戴路","虹莘路","七莘路"]
delay12 = [4,2,2,3,2,3,2,2,3,2,2,2,2,4,2,3,3,3,2,2,3,3,2,3,2,2,2,3,2,3,2]
for i in range(len(line12)):
  S.append(station(line12[i],12))
for i in range(len(delay12)):
  path_map[n+i][n+i+1] = (delay12[i],None)
  path_map[n+i+1][n+i] = (delay12[i],None)
n = n+len(line12)


# line 13 -- 19 stations (341-359)
line13 = ["金运路","金沙江西路","丰庄","祁连山南路","真北路","大渡河路","金沙江路","隆德路","武宁路","长寿路","江宁路","汉中路","自然博物馆","南京西路","淮海中路","新天地","马当路","世博会博物馆","世博大道"]
delay13 = [2,3,3,2,3,3,3,3,2,2,3,1,3,2,3,2,2,3]
for i in range(len(line13)):
  S.append(station(line13[i],13))
for i in range(len(delay13)):
  path_map[n+i][n+i+1] = (delay13[i],None)
  path_map[n+i+1][n+i] = (delay13[i],None)
n = n+len(line13)


# line 16 -- 13 stations (360-372)
line16 = ["滴水湖","临港大道","书院","惠南东","惠南","野生动物园","新场","航头东","鹤沙航城","周浦东","罗山路","华夏中路","龙阳路"]
delay16 = [3,6,9,5,6,5,4,3,4,4,4,4]
for i in range(len(line16)):
  S.append(station(line16[i],16))
for i in range(len(delay16)):
  path_map[n+i][n+i+1] = (delay16[i],None)
  path_map[n+i+1][n+i] = (delay16[i],None)
n = n+len(line16)


# Intersections
intersec = [[0,113],[4,58],[5,333],[6,88],[7,224,284],[9,165],[10,257,327],[12,46,200],[14,325,352],[15,70,105],[39,153,372],[42,98,140,216],[45,253],[47,326,354],[48,166],[49,286],[50,65,110],[55,267],[56,268],[60,332],[62,87,225],[63,112,260],[64,111],[66,109,347],[67,108,288],[68,107,169],[69,106],[71,104],[73,204],[90,163],[91,329],[93,196],[96,142],[101,320],[103,250],[131,313],[142,157],[151,191,279],[159,194],[162,330],[164,223],[168,350],[197,219],[198,255],[201,324],[206,248],[220,357],[222,328],[252,323],[256,285],[274,371],[282,331],[287,348]]
path_map1 = path_map[:]
for sec in intersec:
  for i in sec:
    for j in sec:
      if i!=j:
        path_map[i][j] = (0,None)
        path_map1[i][j] = (1000,None)

path_map_1 = Dijkstra(range(S_num),path_map)
# path_map_2 = Dijkstra(range(S_num),path_map1)
# path_map_3 = BellmanFord(range(S_num),path_map)
# path_map_4 = BellmanFord(range(S_num),path_map1)
print path_map_1
print "Please input the starting station in Chinese:"
start = raw_input("起始站：")
print "Please input the destination in Chinese:"
end = raw_input("目的站")

















