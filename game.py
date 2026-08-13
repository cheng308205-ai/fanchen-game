import time

# 初始化玩家状态
player = {
    "name": "无名修士",
    "realm": "炼气一层",
    "xian_ming": 0,  # 仙名（正道声望）
    "xiong_ming": 0, # 凶名（邪修声望）
    "wei_ming": 0    # 威名（中立声望）
}

def show_status():
    print("\n==================================")
    print(f"【道号】{player['name']} | 【境界】{player['realm']}")
    print(f"【声望】仙名：{player['xian_ming']} | 凶名：{player['xiong_ming']} | 威名：{player['wei_ming']}")
    
    # 动态声望评价（对应设计中的世界反应与NPC态度）
    if player["xian_ming"] >= 5:
        print("【世界评价】仙名远播：德高望重，百姓敬仰，隐隐有散修前来投奔。")
    elif player["xiong_ming"] >= 5:
        print("【世界评价】凶名赫赫：不可招惹，凡人惊恐，正道暗中警惕。")
    elif player["wei_ming"] >= 5:
        print("【世界评价】威名莫测：实力深不可测，行踪诡秘。")
    else:
        print("【世界评价】默默无闻：天地广阔，世人尚不知你之名。")
    print("==================================\n")
    time.sleep(1)

def chapter_one():
    print("📜 第一章：凡尘惊蛰")
    print("细雨镇街头，黑虎帮泼皮正欲对怀抱灵草的孤苦少年下毒手……")
    print("1. 拔剑出手，斩杀泼皮，救下少年（+仙名）")
    print("2. 强势出手，残忍抹杀泼皮，夺走灵草（+凶名）")
    print("3. 指尖弹出一道暗劲，震慑全场，深藏功与名离去（+威名）")
    
    choice = input("\n请做出你的选择 (输入数字 1、2 或 3): ")
    
    if choice == "1":
        player["xian_ming"] += 5
        print("\n你出手救下少年。百姓交口称赞，你的仙名大涨！")
    elif choice == "2":
        player["xiong_ming"] += 5
        print("\n你手段狠辣，夺宝杀人。周围凡人吓得瑟瑟发抖，你的凶名传开。")
    elif choice == "3":
        player["wei_ming"] += 5
        print("\n你展露莫测实力不留姓名，镇中高手对你忌惮万分，威名初显。")
    else:
        print("\n你选择袖手旁观，悄然离去，世界因果未起。")

def main():
    print("================================")
    print("    《凡尘仙役》云端测试版      ")
    print("================================")
    
    player["name"] = input("请输入你的道号: ")
    print(f"\n天道轰鸣，修仙之路开启，你的选择将决定一生的名望。")
    
    show_status()
    chapter_one()
    show_status()
    
    print("【第一阶段底层测试完毕！后续可继续扩展地图与NPC互动。】")

if __name__ == "__main__":
    main()

