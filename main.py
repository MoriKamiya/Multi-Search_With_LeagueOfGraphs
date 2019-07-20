import webbrowser

ID_Mem = []
error_Mem = []
ID_Query = ""
temp = ""
LOG_URL = "https://www.leagueofgraphs.com/summoner/tw/"
while 1:
    original_Str = input("Ready: \r\n")
    while original_Str != "":
        if original_Str[len(original_Str)-6 : len(original_Str)] == "進入組隊房間":
            temp = original_Str.replace("進入組隊房間","").strip()
        elif original_Str[len(original_Str)-6 : len(original_Str)] == "離開組隊房間":
            temp = original_Str.replace("離開組隊房間","").strip()    
        elif ":  " in original_Str: 
            temp = original_Str.split(":", 1)
            temp = temp[0].strip()
        else:
            error_Mem.append(original_Str)
        if temp in ID_Mem:
            """NOP"""
        else:
            if temp != "":
                ID_Mem.append(temp)
                temp = ""
        original_Str = input()
    for i in range(0,len(error_Mem)):
        error_String = error_Mem.pop()
        print("Error content format!:\r\n" + error_String)
    while len(ID_Mem)!= 0:
        if len(ID_Mem) == 0:
            break
        ID_Query = ID_Mem.pop()
        webbrowser.open(LOG_URL + ID_Query, new = 0)

"""
AAA 進入組隊房間
BBB 進入組隊房間
CCC 進入組隊房間
DDD 進入組隊房間
EEE 進入組隊房間
"""
        




