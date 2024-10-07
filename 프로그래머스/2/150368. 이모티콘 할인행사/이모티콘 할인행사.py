from itertools import product

def solution(users, emoticons):
    # 할인율 후보들
    discount_rates = [10, 20, 30, 40]
    max_subscribers = 0  # 최대 이모티콘 플러스 가입자 수
    max_sales = 0        # 최대 이모티콘 판매 금액

    # 이모티콘별 할인율 조합을 모두 생성 (각 이모티콘에 대해 10%, 20%, 30%, 40% 중 하나 선택)
    discount_combinations = list(product(discount_rates, repeat=len(emoticons)))

    # 모든 할인율 조합에 대해 계산
    for discounts in discount_combinations:
        total_subscribers = 0  # 현재 조합에서의 이모티콘 플러스 가입자 수
        total_sales = 0        # 현재 조합에서의 총 판매 금액

        # 각 사용자에 대해 계산
        for rate, threshold in users:
            user_total = 0  # 이 사용자의 이모티콘 구매 총액

            # 각 이모티콘에 대해 할인율을 적용하여 구매할지 판단
            for i in range(len(emoticons)):
                if discounts[i] >= rate:  # 할인율이 사용자의 기준을 충족하면
                    user_total += emoticons[i] * (100 - discounts[i]) / 100  # 이모티콘 구매

            # 구매한 총액이 사용자의 이모티콘 플러스 가입 기준을 넘으면 가입
            if user_total >= threshold:
                total_subscribers += 1
            else:
                total_sales += user_total  # 이모티콘만 구매한 경우

        # 현재 할인율 조합에서의 결과가 더 좋으면 갱신
        if total_subscribers > max_subscribers or (total_subscribers == max_subscribers and total_sales > max_sales):
            max_subscribers = total_subscribers
            max_sales = total_sales

    return [max_subscribers, int(max_sales)]  # 총 가입자 수와 판매 금액 반환