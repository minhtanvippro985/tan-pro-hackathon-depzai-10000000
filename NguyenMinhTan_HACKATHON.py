players_list = [
    {
        "player_id" : "CT007",
        "player_name": "Nguyen Quang Hai",
        "matches": 10,
        "goals":5,
        "assits":4,
        "performance_score": 33,
        "title" : "Trụ cột đội bóng"
    }
]



def display_players(list_here):
    if len(list_here) == 0:
        print("hiien danh sách đang trống")
    else:
        for players in list_here:
            print(f"Mã : {players['player_id']} | Tên : {players['player_name']} | Số trận : {players['matches']} | Số bàn : {players['goals']} | Kiến tạo : {players['assits']} | Hiệu suất : {players['performance_score']} | Phong độ : {players['title']} ")


def validate_number(number_input):
    if number_input < 0:
        return False
    else:
        return True

def performance_cal(matches , goals , assits):
    return (matches * 1) + (goals * 3) + (assits * 2)

def title_check(avg_score):
   if avg_score >= 30 and avg_score < 50:
       return "Trụ cột đội bóng"
   elif avg_score >= 15 and avg_score < 30:
       return "Dự bị chiến lược"
   elif avg_score > 50:
       return "Ngôi sao đẳng cấp"
   else:
       return "Cần thanh lý"

def players_in_list(id_input , list_here):
    found = False
    for index,players in enumerate(list_here , start=0):
        if players['player_id'] == id_input:
            found == True
            return index
    if found == False:
        return -1

def add_new_player(list_here):
    new_player_id = input("Nhập mã cầu thủ mới : ").strip().upper()
    if new_player_id == "":
        print("Mã không được để trống")
        return


    if players_in_list(new_player_id ,list_here) != -1 :
        print(f"{new_player_id} đã tồn tại trong danh sách!")
        return
    else:
        print("---- ĐƯỢC NHẬP TIẾP ----")
        new_player_name = input("Nhập tên cầu thủ mới : ").strip().title()
        if new_player_name == "":
            print("Tên không được để trống!")
            return
        try:
            new_matches_input = int(input("Nhập số trận của cầu thủ đó : "))
        except ValueError:
            print("Nhập sai định dạng")
            return
        if not validate_number(new_matches_input):
            print("Số nhập vào phải là một số dương!")
            return
        
        try:
            new_goals_input = int(input("Nhập số bàn của cầu thủ đó : "))
        except ValueError:
            print("Nhập sai định dạng")
            return
        if not validate_number(new_goals_input):
            print("Số nhập vào phải là một số dương!")
            return
        
        try:
            new_assits_input = int(input("Nhập số kiến tạo của cầu thủ đó : "))
        except ValueError:
            print("Nhập sai định dạng")
            return
        if not validate_number(new_assits_input):
            print("Số nhập vào phải là một số dương!")
            return
        avg_calculate = performance_cal(new_matches_input , new_goals_input , new_assits_input)
        new_player_properties = {         
            "player_id" : new_player_id,
            "player_name": new_player_name,
            "matches": new_matches_input,
            "goals": new_goals_input,
            "assits":4,
            "performance_score": avg_calculate,
            "title" : title_check(avg_calculate)
        }
        list_here.append(new_player_properties)

def update_player(list_here):
    input_find_id = input("Nhập mã cầu thủ cần cập nhật :  ").strip().upper()
    if input_find_id =="":
        print("Không được để trống thông tin!")
        return
    if players_in_list(input_find_id,list_here) != -1:
        print(f"Đã tìm thấy {input_find_id} trong danh sách!")
        try:
            new_matches_update = int(input("Nhập số trận của cầu thủ đó : "))
        except ValueError:
            print("Nhập sai định dạng")
            return
        if not validate_number(new_matches_update):
            print("Số nhập vào phải là một số dương!")
            return
        
        try:
            new_goals_update = int(input("Nhập số bàn của cầu thủ đó : "))
        except ValueError:
            print("Nhập sai định dạng")
            return
        if not validate_number(new_goals_update):
            print("Số nhập vào phải là một số dương!")
            return
        
        try:
            new_assits_update = int(input("Nhập số kiến tạo của cầu thủ đó : "))
        except ValueError:
            print("Nhập sai định dạng")
            return
        if not validate_number(new_assits_update):
            print("Số nhập vào phải là một số dương!")
            return
        avg_update = performance_cal(new_matches_update , new_goals_update , new_assits_update)
        list_here[players_in_list(input_find_id,list_here)].update({
            "matches": new_matches_update,
            "goals": new_goals_update,
            "assits":new_assits_update,
            "performance_score": avg_update,
            "title" : title_check(avg_update)
        })
        print(f"Đã cập nhật thành công cầu thủ  {input_find_id} ")
    else:
        print(f"{input_find_id} Không tồn tại trong danh sách!")
        return
        
def delete_player(list_here):
    input_delete_id = input("Nhập mã cầu thủ cần Xóa :  ").strip().upper()
    if input_delete_id =="":
        print("Không được để trống thông tin!")
        return
    if players_in_list(input_delete_id,list_here) != -1:
        print(f"Đã tìm thấy {input_delete_id} trong danh sách!")
        while True:
            delete_choice = input(f"Bạn có muốn thanh lý cầu thủ không??\ny.Có\nn.không").strip().lower()
            if delete_choice == "y":
                print(f"Đã thanh lý cầu thủ {input_delete_id}")
                list_here.pop(players_in_list(input_delete_id,list_here))
                return
            elif delete_choice == "n":
                print("Đã hủy xóa")
                return
            else:
                print("Vui lòng chọn y hoặc n..")
                continue
    else:
        print(f"Không tìm thấy {input_delete_id} trong danh sách!")
        return

def find_players(list_here):
    input_find_players = input("Nhập mã hoặc là tên cầu thủ để tìm : ").lower().strip()
    count = 0
    for index,players in enumerate(list_here , start=0):
        if players['player_name'].lower().startswith(input_find_players) or players['player_id'].lower() == input_find_players or players['player_name'].lower().count(input_find_players):
            count = count + 1
            print(f"Mã : {players['player_id']} | Tên : {players['player_name']} | Số trận : {players['matches']} | Số bàn : {players['goals']} | Kiến tạo : {players['assits']} | Hiệu suất : {players['performance_score']} | Phong độ : {players['title']} ")
    if count == 0:
        print("Không có kết quả nào phù hợp...")

def statistics_player(list_here):
    can_thanh_ly = 0
    du_bi_chienluoc = 0
    tru_cot_doi = 0
    ngoi_sao = 0
    for players in list_here:
        if players['title'] == "Cần thanh lý":
            can_thanh_ly = can_thanh_ly + 1
        elif players['title'] == "Dự bị chiến lược":
            du_bi_chienluoc = du_bi_chienluoc + 1
        elif players['title'] == "Ngôi sao đẳng cấp":
            ngoi_sao = ngoi_sao + 1
        elif players['title'] == "Trụ cột đội bóng":
            tru_cot_doi = tru_cot_doi + 1

    print(f"""
\n
========= THỐNG KÊ ĐỘI BÓNG =============
Số cầu thủ cần thanh lý : {can_thanh_ly}
Số cầu thủ dự bị : {du_bi_chienluoc}
Số trụ cột đội : {tru_cot_doi}
Ngôi sao trong đội : {ngoi_sao}
======================================
""")
        

while True:
    choice = input("""
========================================
1.Hiển thị danh sách cầu thủ
2.Tiếp nhận cầu thủ mới
3.Cập nhật thông tin và chỉ số
4.Xóa cầu thủ
5.Tìm kiếm cầu thủ
6.Thống kê phân loại phong độ
7.Thoát chương trình
===============================


""")
    
    match choice:
        case "7":
            print("Thoát chương trình.....")
            break
        case "1":
            display_players(players_list)
        case "2":
            add_new_player(players_list)
        case "3":
            update_player(players_list)
        case "4":
            delete_player(players_list)
        case "5":
            find_players(players_list)            
        case "6":
            statistics_player(players_list)
        case _ :
            print("Vui lòng nhập từ 1 - 7")
            