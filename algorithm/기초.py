import random
q = 3
q2 = 1
qq = [
    [0.5,   0.5,    0],
    [0.5,   0,      0.5], 
    [0,     0.5,    0.5]
    ]

def get_percentage_list(n):
    percentage_list = []
    for i in range(n):
        # a, b, c = map(float, input().split())
        a, b, c = [qq[i][0],qq[i][1],qq[i][2]]
        percentage =sorted({'a':a, 'b':b, 'c':c}.items(), key=lambda x: x[1])
        percentage_list.append(percentage)
    return percentage_list

    
# 유저 한명의 행동 정하기
def get_users_action(p_list, n):
    users_actions = {'a':[], 'b':[], 'c':[]}
    # 모든 유저의 액션 설정
    while True:
        for i in range(n):
            add_user_rand = 0.0
            # 유저 한명의 액션 설정
            for j,_ in enumerate(p_list):
                rand = round(random.random(),3)
                add_user_rand += p_list[i][j][1]
                # 랜덤값 찾으면
                if rand < add_user_rand:
                    user_action = p_list[i][j][0]
                    user = {'user':i, 'action':user_action}
                    users_actions[user_action].append(user)
                    break
        if not (users_actions['a'] and users_actions['b'] and users_actions['c']):
            break
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

def dfs_win(winners,n):
    percentage_list = get_percentage_list(n)
    actions = get_users_action(percentage_list, len(winners) )
    winners, losers = get_winner_loser(actions)

    # actions = 
    # winner, loser = get_winner_loser(winners)
    
    
def main():
    # n = 참가자, k = 등수
    # n, k = map(int, input().split())
    n, k = [q,q2]
    percentage_list = get_percentage_list(n)
    actions = get_users_action(percentage_list, n )
    winners, losers = get_winner_loser(actions)
    dfs_win(winners,n)
    
main()