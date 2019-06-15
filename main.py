"""
AAA 進入組隊房間
BBB 進入組隊房間
CCC 進入組隊房間
DDD 進入組隊房間
EEE 進入組隊房間
"""
import webbrowser

ID_Mem = []
ID_Query = ""
temp = ""
LOG_URL = "https://www.leagueofgraphs.com/summoner/tw/"
while 1:
    original_Str = input("Ready: \r\n")
    while original_Str != "":
        if original_Str[len(original_Str)-6 : len(original_Str)] == "進入組隊房間":
            temp = original_Str.replace("進入組隊房間","").strip()
        elif ":  " in original_Str: 
            temp = original_Str.split(":", 1)
            temp = temp[0].strip()
        else:
            print("Error content format!:\r\n" + original_Str)
        if temp in ID_Mem:
            """NOP"""
        else:
            if temp != "":
                ID_Mem.append(temp)
                temp = ""
        original_Str = input()
    while len(ID_Mem)!= 0:
        if len(ID_Mem) == 0:
            break
        ID_Query = ID_Mem.pop()
        webbrowser.open(LOG_URL + ID_Query, new = 0)
        




