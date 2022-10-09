import json
import math
import os
import time
import recipes, items
#import heartrate; heartrate.trace(browser=True)

item_code = {
    "水": 1000,
    "铁矿": 1001,
    "铜矿": 1002,
    "硅石": 1003,
    "钛石": 1004,
    "石矿": 1005,
    "煤矿": 1006,
    "原油": 1007,
    "可燃冰": 1011,
    "金伯利矿石": 1012,
    "分形硅石": 1013,
    "光栅石": 1014,
    "刺笋结晶": 1015,
    "单极磁石": 1016,
    "木材": 1030,
    "植物燃料": 1031,
    "铁块": 1101,
    "磁铁": 1102,
    "钢材": 1103,
    "铜块": 1104,
    "高纯硅块": 1105,
    "钛块": 1106,
    "钛合金": 1107,
    "石材": 1108,
    "高能石墨": 1109,
    "玻璃": 1110,
    "棱镜": 1111,
    "金刚石": 1112,
    "晶格硅": 1113,
    "精炼油": 1114,
    "塑料": 1115,
    "硫酸": 1116,
    "有机晶体": 1117,
    "钛晶石": 1118,
    "钛化玻璃": 1119,
    "氢": 1120,
    "重氢": 1121,
    "反物质": 1122,
    "石墨烯": 1123,
    "碳纳米管": 1124,
    "框架材料": 1125,
    "卡西米尔晶体": 1126,
    "奇异物质": 1127,
    "地基": 1131,
    "加速剂Mk.I": 1141,
    "加速剂Mk.II": 1142,
    "加速剂Mk.III": 1143,
    "齿轮": 1201,
    "磁线圈": 1202,
    "电动机": 1203,
    "电磁涡轮": 1204,
    "超级磁场环": 1205,
    "粒子容器": 1206,
    "临界光子": 1208,
    "引力透镜": 1209,
    "空间翘曲器": 1210,
    "电路板": 1301,
    "微晶元件": 1302,
    "处理器": 1303,
    "位面过滤器": 1304,
    "量子芯片": 1305,
    "电浆激发器": 1401,
    "粒子宽带": 1402,
    "湮灭约束球": 1403,
    "光子合并器": 1404,
    "推进器": 1405,
    "加力推进器": 1406,
    "太阳帆": 1501,
    "戴森球组件": 1502,
    "小型运载火箭": 1503,
    "液氢燃料棒": 1801,
    "氘核燃料棒": 1802,
    "反物质燃料棒": 1803,
    "传送带": 2001,
    "高速传送带": 2002,
    "极速传送带": 2003,
    "分拣器": 2011,
    "高速分拣器": 2012,
    "极速分拣器": 2013,
    "四向分流器": 2020,
    "小型储物仓": 2101,
    "大型储物仓": 2102,
    "行星内物流运输站": 2103,
    "星际物流运输站": 2104,
    "轨道采集器": 2105,
    "储液罐": 2106,
    "物流配送器": 2107,
    "电力感应塔": 2201,
    "无线输电塔": 2202,
    "风力涡轮机": 2203,
    "火力发电厂": 2204,
    "太阳能板": 2205,
    "蓄电器": 2206,
    "蓄电器（满）": 2207,
    "射线接收站": 2208,
    "能量枢纽": 2209,
    "人造恒星": 2210,
    "微型聚变发电站": 2211,
    "卫星配电站": 2212,
    "采矿机": 2301,
    "电弧熔炉": 2302,
    "制造台Mk.I": 2303,
    "制造台Mk.II": 2304,
    "制造台Mk.III": 2305,
    "抽水站": 2306,
    "原油萃取站": 2307,
    "原油精炼厂": 2308,
    "化工厂": 2309,
    "微型粒子对撞机": 2310,
    "电磁轨道弹射器": 2311,
    "垂直发射井": 2312,
    "喷涂机": 2313,
    "分馏塔": 2314,
    "位面熔炉": 2315,
    "大型采矿机": 2316,
    "量子化工厂": 2317,
    "矩阵研究站": 2901,
    "物流运输机": 5001,
    "星际物流运输船": 5002,
    "配送运输机": 5003,
    "电磁矩阵": 6001,
    "能量矩阵": 6002,
    "结构矩阵": 6003,
    "信息矩阵": 6004,
    "引力矩阵": 6005,
    "宇宙矩阵": 6006,
}

aux_belt = {
    "header": {
        "index": 999999,
        "area_index": 0,
        "local_offset_x": 0.0,
        "local_offset_y": 1.0000013,
        "local_offset_z": 48.00001,
        "local_offset_x2": 0.0,
        "local_offset_y2": 1.0000013,
        "local_offset_z2": 48.00001,
        "yaw": -0.00053655176,
        "yaw2": -0.00053655176,
        "item_id": 2003,
        "model_index": 37,
        "output_object_index": 4294967295,
        "input_object_index": 4294967295,
        "output_to_slot": 1,
        "input_from_slot": 0,
        "output_from_slot": 0,
        "input_to_slot": 1,
        "output_offset": 0,
        "input_offset": 0,
        "recipe_id": 0,
        "filter_id": 0,
        "parameter_count": 0
    },
    "param": {
        "Belt": {"label": 405, "count": 8}
    }
}
sorter_buildings = [2101, 2102, 2302, 2315, 2303, 2304, 2305, 2308, 2309, 2310,2317, 2901, 2311, 2312, 2210]
recipe_buildings = [2302, 2315, 2303, 2304, 2305, 2308, 2309, 2310,2317]

belt_buildings = [2020, 2103, 2104, 2208, 2209]
items_belts = [2001, 2002, 2003]
items_sorter = [2011, 2012, 2013]

belt_count_mode = 0  # 0输出爪子个数，1输出每秒需要的数量（向上取整）


class Belt:
    def __init__(self, building):
        self.index = building['header']['index']
        self.type = building['header']['item_id']
        self.label = self.get_label(building)
        self.sorters = []
        self.next_index = 4294967295

    def get_label(self, building):
        if 'Belt' in building['param']:
            if 'label' in building['param']['Belt']:
                return building['param']['Belt']['label']
        return 0

    def get_header(self, buildings):
        pass


class Belts:
    def __int__(self, buildings):
        self.belts = []
        pass


class Building:
    def __init__(self):
        pass


def get_buildings(path):
    with open(path, "r") as f:
        params = json.load(f)
        buildings = params["data"]["buildings"]

    return buildings, params


def set_json(txt, dicts):
    txt += '_无带.json'
    with open(txt, "w") as r:
        json.dump(dicts, r)


def get_building_by_index(buildings, index):
    if index == 4294967295:
        return 4294967295
    if index < len(buildings):
        if buildings[index]['header']['index'] == index:
            return buildings[index]
    for b in buildings:
        if b['header']['index'] == index:
            return b


# 似乎没有用
def get_outbelt_buildings(buildings):
    outbelt = [b for b in buildings if b['header']['item_id'] in belt_buildings]
    return outbelt


def get_recipe_by_index(buildings, index, s_filter, io):
    recipe_id = 0
    mode_text = ['增产', '加速', '未知']
    mode = 2
    item_name = '未知建筑'
    s_name = '未知物品'
    for k, v in item_code.items():
        if v == s_filter:
            s_name = k
    rp = []

    if index != 4294967295:
        if index < len(buildings):
            if buildings[index]['header']['index'] == index:
                b = buildings[index]
                recipe_id = b['header']['recipe_id']
                if b['header']['item_id'] == 2901:
                    mode = b['param']['Unknown'][1]
                if b['header']['item_id'] in recipe_buildings:
                    mode = b['param']['Unknown'][0]
                for k, v in item_code.items():
                    if v == b['header']['item_id']:
                        item_name = k

        else:
            for b in buildings:
                if b['header']['index'] == index:
                    recipe_id = b['header']['recipe_id']
                    if b['header']['item_id'] == 2901:
                        mode = b['param']['Unknown'][1]
                    if b['header']['item_id'] in recipe_buildings:
                        mode = b['param']['Unknown'][0]
                    for k, v in item_code.items():
                        if v == b['header']['item_id']:
                            item_name = k

    if recipe_id == 0 or recipe_id > 121:
        rname = '错误'
        inputs_by_sec = []
        outputs_by_sec = []
        if item_name == '微型聚变发电站':
            print('Warning:绿棒燃烧需求未经过严格计算，相关数值可能不准确')
            rname = '绿棒'
            inputs_by_sec = [1802, 0.05]
            pass
        if item_name == '人造恒星':
            rname = '黑棒'
            inputs_by_sec = [1803, 0.02]
            pass
        if item_name == '电磁轨道弹射器':
            rname = '太阳帆'
            inputs_by_sec = [1501, 40.0 / 60.0]
            pass
        if item_name == '垂直发射井':
            rname = '小火箭'
            inputs_by_sec = [1503, 10 / 60]
            pass
        if item_name == '矩阵研究站':
            rank = research_rank
            inputs_by_sec = [6006, rank]
            pass
        if item_name == '小型储物仓' or item_name == '大型储物仓':
            print('Warning:储物仓仅支持单种物品，仅支持同一物品进出，若有多个物品仅支持第一个检测到的物品')
            if s_name == '未知物品':
                print('Warning:分拣器处理物品代号为{0}但本程序未收录，可能无法处理'.format(s_filter))
            if s_filter == 0:
                print('Warning:进出储物仓的分拣器没有设置filter，忽略处理')
            if s_filter > 0:
                print('Warning:储物仓对{0}物品进仓按照120/s进行计算，出仓按照30/s进行计算，相关数值统计可能不准确'.format(s_name))
                inputs_by_sec = [s_filter, 120]
                outputs_by_sec = [s_filter, 30]
            pass
        if item_name == '火力发电厂':
            print('Warning:尚未实现检查是否可燃，需要自行检查，相关数值统计可能不准确')
            if io == 'input' and s_filter > 0:
                inputs_by_sec = [s_filter, 30]
            if io == 'output' and s_filter > 0:
                outputs_by_sec = [s_filter, 30]
            pass
        if item_name == '传送带' or item_name == '高速传送带' or item_name == '极速传送带':
            print('Warning:传送带上的分拣器对{0}物品需求按照120/s进行计算，输出按照30/s进行计算，相关数值统计可能不准确，仅支持单工'.format(s_name))
            if s_filter == 0:
                print('Warning:进出传送带的分拣器没有设置filter，忽略处理')
            if io == 'input' and s_filter > 0:
                inputs_by_sec = [s_filter, 120]
            if io == 'output' and s_filter > 0:
                outputs_by_sec = [s_filter, 30]
            pass

        rp = [item_name, -1, '消耗' + rname, mode_text[mode], inputs_by_sec, outputs_by_sec]

    input_muti = 1
    output_muti = 1
    for r in recipes.game_recipes:
        if r['id'] == recipe_id:

            rp = [item_name, r['id'], r['name'], mode_text[mode], r['inputs_by_sec'].copy(), r['outputs_by_sec'].copy()]

            if item_name == '制造台Mk.III':
                input_muti = 1.5
                output_muti = 1.5
            if item_name == '制造台Mk.I':
                input_muti = 0.75
                output_muti = 0.75
            if item_name == '位面熔炉':
                input_muti = 2
                output_muti = 2

            if mode == 0:
                output_muti *= 1.25
            if mode == 1:
                input_muti *= 2
                output_muti *= 2
            for i in range(len(rp[4])):
                if rp[4][i] < 999:
                    rp[4][i] *= input_muti
            for i in range(len(rp[5])):
                if rp[5][i] < 999:
                    rp[5][i] *= output_muti
            break

    return rp


# [item_id,[原料输入],[成品输入]...]
def get_marked_belts(buildings):
    print("正在取得带标签的传送带")
    # belts = [b for b in buildings if 'Belt' in b['param'] and b['header']['parameter_count'] == 2]
    stations = [b for b in buildings if b['header']['item_id'] in [2103, 2104]]

    def check_belt(b):
        if b['header']['item_id'] not in items_belts:
            return False
        if b['header']['parameter_count'] < 2:
            return False
        # print(b)
        for s in stations:
            sx = s['header']['local_offset_x']
            sy = s['header']['local_offset_y']
            sz = s['header']['local_offset_z']
            bx = b['header']['local_offset_x']
            by = b['header']['local_offset_y']
            bz = b['header']['local_offset_z']
            dx = abs(sx - bx)
            dy = abs(sy - by)
            dz = abs(sz - bz)
            if dx < 3.5 and dy < 3.5 and dz < 1:
                # print('belt_deleted')
                return False
        return True

    for s in stations:
        # print(s)
        pass
    if stations:
        print("存在物流站{0}，已经剔除物流站内含标签的传送带".format(len(stations)))
    else:
        print('未检测到物流站')
    print('正在按物品生成传送带')
    # belts = [b for b in belts if b['param']['Belt']]
    belts = [[b['param']['Belt']['label'], b['header']['index']] for b in buildings if check_belt(b)]
    for b in belts:
        # print(b)
        pass

    belts_by_item = []

    # belts_by_item_belts_index=[]

    def is_input_to_sorter(index):
        building = get_building_by_index(buildings, index)
        if (building['header']['output_object_index'] < 4294967295 and building['header']['parameter_count'] == 2):
            return is_input_to_sorter(building['header']['output_object_index'])
        if (building['header']['output_object_index'] == 4294967295 and building['header']['parameter_count'] == 2):
            return True
        if (building['header']['output_object_index'] < 4294967295 and building['header']['parameter_count'] != 2):
            return False
        if (building['header']['output_object_index'] == 4294967295 and building['header']['parameter_count'] != 2):
            return False
        print('传送带设置错误')
        print(building)
        os.system("pause")

    for b in belts:

        if b[0] not in belts_by_item:
            belts_by_item.append(b[0])
            if is_input_to_sorter(b[1]):
                belts_by_item.append([b[1]])
                belts_by_item.append([])
            else:
                belts_by_item.append([])
                belts_by_item.append([b[1]])

        else:
            if is_input_to_sorter(b[1]):
                belts_by_item[belts_by_item.index(b[0]) + 1].append(b[1])
            else:
                belts_by_item[belts_by_item.index(b[0]) + 2].append(b[1])

    # print(belts_by_item)
    print('已生成{0}个物品传送带'.format(int(len(belts_by_item) / 3)))
    return belts, belts_by_item


# [建筑id,[配方参数],[输入建筑的分拣器id],[从建筑输出的分拣器id]...]
def get_sorters(buildings):
    print('正在从{0}个建筑中取得分拣器'.format(len(buildings)))
    sorters = [b for b in buildings if
               b['header']['item_id'] in [2011, 2012, 2013]]
    sorters_by_building = []
    print('已取得{0}个分拣器'.format(len(sorters)))
    print('正在以建筑为索引，索引分拣器')
    for s in sorters:
        if s['header']['input_object_index'] + s['header']['output_object_index'] < 4294967295:
            print('存在两端均连接的分拣器{0}，跳过'.format(s['header']['index']))
            continue
        if s['header']['input_object_index'] == s['header']['output_object_index']:
            print('存在两端都未连接的分拣器{0}，跳过'.format(s['header']['index']))
            continue
        if s['header']['input_object_index'] < 4294967295:
            if s['header']['input_object_index'] not in sorters_by_building:
                sorters_by_building.append(s['header']['input_object_index'])
                sorters_by_building.append(
                    get_recipe_by_index(buildings, s['header']['input_object_index'], s['header']['filter_id'],
                                        'output'))
                sorters_by_building.append([])
                sorters_by_building.append([s['header']['index']])
            else:
                sorters_by_building[sorters_by_building.index(s['header']['input_object_index']) + 3].append(
                    s['header']['index'])
                pass
        if s['header']['output_object_index'] < 4294967295:
            if s['header']['output_object_index'] not in sorters_by_building:
                sorters_by_building.append(s['header']['output_object_index'])
                sorters_by_building.append(
                    get_recipe_by_index(buildings, s['header']['output_object_index'], s['header']['filter_id'],
                                        'input'))
                sorters_by_building.append([s['header']['index']])
                sorters_by_building.append([])
            else:
                sorters_by_building[sorters_by_building.index(s['header']['output_object_index']) + 2].append(
                    s['header']['index'])
                pass

    # print(sorters_by_building)
    print('分拣器获取完成，共计{0}个分拣器，{1}个设备'.format(len(sorters), int(len(sorters_by_building) / 4)))
    return sorters, sorters_by_building


# [带子id,[分拣器id...],[分拣器需求量]]
# 额外产出建筑output[1.125,1.2,1.25]
# 加速生产建筑input[1.25,1.5,2]
def set_sorters(sorters_by_building, belts_by_item, params):
    print('正在设置分拣器')
    lt = time.time()
    ot=lt
    io_belts = []
    for b in belts_by_item:
        if isinstance(b, list):
            for bb in b:
                io_belts.append(bb)
                io_belts.append([])
    # print(io_belts)
    # print(sorters_by_building)
    p_step = int(len(sorters_by_building) / 20)
    if p_step < 1:
        p_step = 1
    for i in range(0, len(sorters_by_building), 4):
        if i % p_step == 0:
            print('正在处理第{0}个分拣器'.format(int(i / 4)))
        nt = time.time()
        dt = nt - lt
        if i > 0 and dt > 60:
            lt = nt
            print('处理速度约为{0}个每分钟'.format(i / 4 / (nt-ot) * 60))
        b_index = sorters_by_building[i]
        b_name = sorters_by_building[i + 1][0]
        rin = sorters_by_building[i + 1][4]
        rout = sorters_by_building[i + 1][5]
        sin = sorters_by_building[i + 2]
        sout = sorters_by_building[i + 3]

        if len(rin) != len(sin) * 2:
            print('Warning:建筑【{0}】index={1}【输入】用分拣器数量不相等，配方有{2}种物品，分拣器有{3}个！'.format(b_name, b_index, int(len(rin) / 2),
                                                                                     len(sin)))
        if len(rout) != len(sout) * 2:
            print(
                'Warning:建筑【{0}】index={1}【输出】用分拣器数量不相等，配方有{2}种物品，分拣器有{3}个！'.format(b_name, b_index, int(len(rout) / 2),
                                                                                   len(sout)))
        # print([rmode, rin, rout, sin, sout])

        # print([rin, rout, sin, sout])

        for k in range(len(sin)):
            sorter_index = sin[k]
            sorter_item = rin[(k * 2) % len(rin)]
            sl = len(sin)
            rl = int(len(rin) / 2)
            amount_ratio = sl // rl
            if (k % rl) < (sl % rl):
                amount_ratio += 1
            sorter_amount = rin[(k * 2) % len(rin) + 1] / amount_ratio

            item_name = '未知'
            for key, value in item_code.items():
                if value == sorter_item:
                    item_name = key
            if sorter_item not in belts_by_item:
                print("FATAL:有设备{0}【需求】物品【{1}】输入，但没有对应的传送带".format(b_name, item_name))
                input('按回车键结束')
                quit(0)
            belts_input = belts_by_item[belts_by_item.index(sorter_item) + 1]
            if not belts_input:
                print("FATAL:有设备{0}【需求】物品【{1}】输入，但对应的传送带长度0".format(b_name, item_name))
                input('按回车键结束')
                quit(0)

            def get_min_belt(bs):
                b_min = 99999
                b_index = bs[0]
                sorter_sum = 0

                for b in bs:
                    m = io_belts.index(b)
                    if io_belts[m + 1] == []:
                        return b
                    else:
                        item_sum = 0
                        sorter_sum = 0
                        for n in io_belts[m + 1]:
                            item_sum += n[1]
                            sorter_sum += 1
                        if item_sum < b_min and sorter_sum < 8:
                            b_min = item_sum
                            b_index = b
                if sorter_sum > 7:
                    print(
                        "ERROR:物品【{0}】在传送带编号{1}处连接了{2}个分拣器，超过了游戏允许8个的上限".format(item_name, b_index, sorter_sum))
                if b_min > 30:
                    print("Warning:物品【{0}】在传送带编号{1}处需求量为{2}，超过了每秒30".format(item_name, b_index, b_min))
                if b_min > 120:
                    print("ERROR:物品【{0}】在传送带编号{1}处需求量为{2}，超过了单带极限每秒120".format(item_name, b_index, b_min))

                return b_index

            b_min = get_min_belt(belts_input)
            io_belts[io_belts.index(b_min) + 1].append([sorter_index, sorter_amount])

        for k in range(len(sout)):
            sorter_index = sout[k]
            sorter_item = rout[(k * 2) % len(rout)]
            if len(rout) > 2:
                s_b = get_building_by_index(params["data"]["buildings"], sorter_index)
                s_b['header']['filter_id'] = sorter_item
            sl = len(sout)
            rl = int(len(rout) / 2)
            amount_ratio = sl // rl
            if (k % rl) < (sl % rl):
                amount_ratio += 1
            sorter_amount = rout[(k * 2) % len(rout) + 1] / amount_ratio

            item_name = '未知'
            for key, value in item_code.items():
                if value == sorter_item:
                    item_name = key
            if sorter_item not in belts_by_item:
                print("FATAL:有设备{0}【出产】物品【{1}】输出，但没有对应的传送带".format(b_name, item_name))
                input('按回车键结束')
                quit(0)
            belts_output = belts_by_item[belts_by_item.index(sorter_item) + 2]
            if not belts_output:
                print("FATAL:有设备{0}【出产】物品【{1}】输出，但对应的传送带长度0".format(b_name, item_name))
                input('按回车键结束')
                quit(0)

            def get_min_belt(bs):
                assert bs != []
                b_min = 99999
                b_index = bs[0]
                sorter_sum = 0
                for b in bs:
                    m = io_belts.index(b)
                    if io_belts[m + 1] == []:
                        return b
                    else:
                        item_sum = 0
                        sorter_sum = 0
                        for n in io_belts[m + 1]:
                            item_sum += n[1]
                            sorter_sum += 1
                        if item_sum < b_min and sorter_sum < 8:
                            b_min = item_sum
                            b_index = b
                if sorter_sum > 7:
                    print(
                        "ERROR:物品【{0}】在传送带编号{1}处已经连接了{2}个分拣器，再连接会超过了游戏允许8个的上限".format(item_name, b_index,
                                                                                      sorter_sum))
                if b_min >= 30:
                    print("Warning:物品【{0}】在传送带编号{1}处需求量为{2}，超过了每秒30".format(item_name, b_index, b_min))
                return b_index

            b_min = get_min_belt(belts_output)
            io_belts[io_belts.index(b_min) + 1].append([sorter_index, sorter_amount])

        for m in range(0, len(io_belts), 2):
            b_item_sum = 0
            b_sorter_sum = 0
            for n in io_belts[m + 1]:
                b_item_sum += n[1]
                b_sorter_sum += 1
            b_b = get_building_by_index(params["data"]["buildings"], io_belts[m])
            if belt_count_mode == 1:
                b_b['param']['Belt']['count'] = b_sorter_sum
            if belt_count_mode == 2:
                b_b['param']['Belt']['count'] = math.ceil(b_item_sum * 60)
            if belt_count_mode == 3:
                b_b['param']['Belt']['count'] = 0
                b_b['param']['Belt']['label'] = 0

            # print("分拣器{0}在传送带{1}处对物品{2}")
            # print([sorter_index, sorter_item, sorter_amount,belts_input])

    # print(io_belts)

    def set_io(b_index, s_index):
        b_s = get_building_by_index(params["data"]["buildings"], s_index)
        if b_s['header']['output_object_index'] == 4294967295:
            b_s['header']['output_object_index'] = b_index
            b_s["header"]["output_to_slot"] = -1
        if b_s['header']['input_object_index'] == 4294967295:
            b_s['header']['input_object_index'] = b_index
            b_s["header"]["input_from_slot"] = -1

    for i in range(0, len(io_belts), 2):
        b_index = io_belts[i]
        for j in io_belts[i + 1]:
            set_io(b_index, j[0])

    print('分拣器设置完成')


# 删除一级带，使用时先降级不需要的传送带
def del_belts(params):
    old_buildings = params["data"]["buildings"]
    new_buildings = [b for b in old_buildings if b['header']['item_id'] not in items_belts]
    new_buildings.append(aux_belt)
    params["data"]["buildings"] = new_buildings
    sorters = [b for b in new_buildings if b['header']['item_id'] in items_sorter]

    def check_index(index):

        for b in new_buildings:
            if b['header']['index'] == index:
                return index
        return 999999

    for s in sorters:
        s['header']['output_object_index'] = check_index(s['header']['output_object_index'])
        s['header']['input_object_index'] = check_index(s['header']['input_object_index'])


def down_belts(buildings):
    for b in buildings:
        if b['header']['item_id'] in items_belts:
            b['header']['item_id'] = items_belts[0]


# 分为三种状态：未连接、传送带、建筑
# output_object_index=4294967295说明分拣器输出未连接，否则连接物品index
# input_object_index=4294967295说明分拣器输入未连接

def gen_no_belts(buildings, params):
    # print([b["header"]["index"] for b in buildings])
    belts, belts_by_item = get_marked_belts(buildings)
    # print(belts)
    sorters, sorters_by_building = get_sorters(buildings)
    # print(sorters)
    set_sorters(sorters_by_building, belts_by_item, params)


print('注意事项：')
print('Warning=不影响脚本流程，但很可能影响蓝图完整功能的内容')
print('ERROR=可能影响脚本流程，也影响蓝图完整功能的内容')
print('FATAL=影响脚本流程，也影响蓝图完整功能')
print('1、不允许有两端未连接或者一端连接在传送带的分拣器')
print('2、支持打火箭、打帆、小太阳装燃料，默认涂增产Mk3，暂不支持锅、能量枢纽等无带')
print('3、建筑缺少输入、输出会提醒')
print('4、每个传送带节点最多只能连接8个分拣器')
print('5、如果没有生成文件，请检查上述问题')
print('6、【不推荐】仓库需要手动指定过滤产物，仅支持单一物品，多个物品会以检测到第一个为准，会造成统计数据的严重偏离，可能会有bug')
print('7、【不推荐】火力发电站需要自行指定过滤产物，会造成相关数据统计不准确，核电不需要自行指定，也会造成统计不准')
print('8、【不推荐】传送带上的分拣器需要自行指定过滤产物，需要一端在无标记的带子，另一边悬空，会造成统计不准确')
print('================')
txt = input("请输入文件名(不需要后缀.txt，需要txt在exe同目录下)：\n")
# txt = '多输出测试'
print(txt)
cmd = '.\\dspbp.exe -i {0}.txt -o {1}.json dump'.format(txt, txt)
print(cmd)

if os.system(cmd) != 0:
    print('转换蓝图到json失败')
    input("请退出..")
    quit()

research_rank = int(input('请输入科研等级（倍率，未升级为1，默认按照15层堆叠计算）：\n'))
print("科研速度为{0}00%".format(research_rank))

buildings, params = get_buildings(txt + '.json')

# method = int(input("请输入模式：1=降级传送带 2=连接分拣器到传送带\n"))
method = 2
if method == 1:
    down_belts(buildings)
    pass

if method == 2:
    belt_count_mode = int(input('请输入标签模式:1=连接到此传送带爪子数量 2=此传送带每分钟需求数量 3=去掉标签\n'))
    # belt_count_mode = 2
    gen_no_belts(buildings, params)

set_json(txt, params)
cmd = '.\\dspbp.exe -i {0}_无带.json -o {1}_无带.txt undump'.format(txt, txt)
if os.system(cmd) != 0:
    print('转换json到蓝图失败')
print(cmd)
input('已生成{0}_无带.txt，点右上角关闭或者输入任意字符退出：'.format(txt))
