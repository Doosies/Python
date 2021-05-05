import random

q = 3
q2 = 1
qq = [
    [0.5, 0.5, 0],
    [0.5, 0, 0.5], 
    [0, 0.5, 0.5],
    [0.5, 0.5, 0],
    [0.5, 0, 0.5], 
    [0, 0.5, 0.5],
    [0.5, 0.5, 0],
    [0.5, 0, 0.5], 
    [0, 0.5, 0.5],
    ]
n, k = [q,q2]
# n, k = map(int, input().split())
rank = []
users_percentage_list = []
cnt = 0

for i in range(n):
        # a, b, c = map(float, input().split())
        a, b, c = [qq[i][0],qq[i][1],qq[i][2]]
        user_action_percentage = {'a':a, 'b':b, 'c':c}
        percentage_actions = sorted(user_action_percentage.items(), key=lambda x: x[1])
        user_dict = {'user':i, 'action':percentage_actions, 'randper':0}
        users_percentage_list.append(user_dict)
# def get_users_percentage_list():
#     percentage_list = []
    
#     return percentage_list

    
# 인자로 들어온 유저들의 액션 설정
def get_users_action(p_list):
    users_actions = {'a':[], 'b':[], 'c':[]}
    while True:
        users_list = []
        for original_user_dict in users_percentage_list:
            for input_user in p_list:
                if original_user_dict['user'] == input_user:
                    users_list.append(original_user_dict)
                    # users_percentage_list[original_user_dict['user']]['randper'] = 0
        # 현재 유조 목록
        for user in users_list:
            add_user_rand = 0.0
            # print(users_percentage_list[user['user']])
            # users_percentage_list[user['user']]['randper'] = 0 
            # 유저 안에 action 목록
            for action in user['action']:
                rand = round(random.random(), 3)
                add_user_rand += action[1]
                if rand < add_user_rand:
                    user_action = action[0]
                    user_name = user['user']
                    users_actions[user_action].append(user_name)
                    if users_percentage_list[user_name]['randper'] == 0:
                        users_percentage_list[user_name]['randper'] += action[1]
                        print(user_name,"더함!")
                    else:
                        users_percentage_list[user_name]['randper'] *= action[1]
                        print(user_name, "곱함")
                    break

        if ((users_actions['a'] and users_actions['b'] 
        or users_actions['b'] and users_actions['c'] 
        or users_actions['c'] and users_actions['a'])
        and not(users_actions['a'] and users_actions['b'] and users_actions['c'])):
            break
        else:
            users_actions = {'a':[], 'b':[], 'c':[]}
            # for user in users_percentage_list:
            #     users_percentage_list[user['user']]['randper'] = 0
        # time.sleep(1.0)
    return users_actions

# 승자 한명 반환666
def get_winner_loser(users_list):
    # a, b, c가 모두 겹치지 않을떄
    # 리턴되는 값은 winner_list, loser_list
    # a는 b를 이김
    # if users_dict['a'] and users_dict['b'] and users_dict['c']:
    if users_list['a'] and users_list['b']:
        return [users_list['a'], users_list['b']]
    # b는 c를 이김
    if users_list['b'] and users_list['c']:
        return [users_list['b'], users_list['c']]
    # c는 a를 이김
    if users_list['c'] and users_list['a']:
        return [users_list['c'], users_list['a']]

def dfs_win(actions):
    users_actions = []
    action = get_users_action(actions)
    # winner, loser = get_winner_loser(action)
    winner_and_loser = get_winner_loser(action)
    for kind in winner_and_loser:
        users_actions = []
        if len(kind) > 1:
            for user in kind:
                users_actions.append(user)
            action = get_users_action(users_actions)
            dfs_win(users_actions)
        else:
            rank.append(kind[0])
    
    if len(winner_and_loser[0]) == 1 and len(winner_and_loser[1]) == 1:
        return


users = list(range(n))
dfs_win(users)
print("rank - > ", rank)
per = [percentage['randper'] for percentage in users_percentage_list]
for val in per:
    print(f'{val:0.20f}', end=' ')
print(sum(per))