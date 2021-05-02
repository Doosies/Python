import random
q = 3
q2 = 1
qq = [
    [1,   0,    0],
    [0,   0,    1], 
    [0,   0,    1]
    ]
n, k = [q,q2]
users_percentage_list = []
for i in range(n):
        # a, b, c = map(float, input().split())
        a, b, c = [qq[i][0],qq[i][1],qq[i][2]]
        user_action_percentage = {'a':a, 'b':b, 'c':c}
        percentage_actions = sorted(user_action_percentage.items(), key=lambda x: x[1])
        user_dict = {'user':i, 'action':percentage_actions}
        users_percentage_list.append(user_dict)

# def get_users_percentage_list():
#     percentage_list = []
    
#     return percentage_list

    
# 모든 유저의 액션 설정
def get_users_action(p_list, n):
    users_actions = {'a':[], 'b':[], 'c':[]}
    while True:
        for i in range(n):
            add_user_rand = 0.0
            # 유저 한명의 액션 설정
            for j,_ in enumerate(p_list):
                rand = round(random.random(),3)
                add_user_rand += p_list[i]['action'][j][1]
                # 랜덤값 찾으면
                if rand < add_user_rand:
                    user_action = p_list[i]['action'][j][0]
                    user = {'user':i, 'action':user_action}
                    users_actions[user_action].append(user)
                    print(users_actions)
                    break
        if not (users_actions['a'] and users_actions['b'] and users_actions['c']):
            break
        else:
            print(users_actions, end='\n')
    return users_actions

# 승자 한명 반환
def get_winner_loser(users_dict):
    # a, b, c가 모두 겹치지 않을떄
    # 리턴되는 값은 winner_list, loser_list
    # a는 b를 이김
    if users_dict['a'] and users_dict['b']:
        return [users_dict['a'], users_dict['b']]
    # b는 c를 이김
    elif users_dict['b'] and users_dict['c']:
        return [users_dict['b'], users_dict['c']]
    # c는 a를 이김
    elif users_dict['c'] and users_dict['a']:
        return [users_dict['c'], users_dict['a']]
    else: 
        return None

def dfs_win(actions):
    
    winner, loser = get_winner_loser(actions)
    if len(winner) > 1:
        print("2명이상이 이김")
    if len(loser) > 1:
        print("2명 이상이 짐")
    print(winner)
    print(loser)
# def main():
    # n = 참가자, k = 등수
    # n, k = map(int, input().split())
    # percentage_list = get_percentage_list(n)
    # actions = get_users_action(percentage_list, n )
    # winners, losers = get_winner_loser(actions)

actions = get_users_action(users_percentage_list, n)
dfs_win(actions)
# percentage_list = get_users_percentage_list()
# print(users_percentage_list)
# dfs_win(winners,n)
# main()