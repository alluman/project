from flask import Flask, render_template, request
import random
import requests
from collections import Counter 
app = Flask(__name__)

@app.route('/')
def home():
    name = '이시문'
    lotto = [16, 18, 22, 43, 32, 11]
    def generate_lotto_numbers():
        return random.sample(range(1, 46), 6)

    if __name__ == "__main__":
        lotto_numbers = generate_lotto_numbers()
        print("로또 번호:", lotto_numbers)

    def count_common_elements(lotto, lotto_numbers):
        # Counter 객체 생성
        counter1 = Counter(lotto)
        counter2 = Counter(lotto_numbers)

    # 두 Counter 객체의 교집합 구하기
        intersection = counter1 & counter2

    # 교집합의 요소 개수 합산
        common_count = sum(intersection.values())

        return common_count

# 두 리스트에서 같은 요소의 개수 확인
    result = count_common_elements(lotto, lotto_numbers)
    print("두 리스트에서 같은 요소의 개수:", result)

    context = {
        "name" : name,
        "lotto" : lotto,
        "lotto_numbers" : lotto_numbers,
        "common_count" : result,
    }
    return render_template('index.html', data=context)

@app.route('/mypage')
def mypage():
    return 'This is Mypage!'

@app.route('/movie')
def movie():
    query = request.args.get('query')

    res = requests.get(
	f"http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=f5eef3421c602c6cb7ea224104795888&movieNm={query}"
    )
    rjson = res.json()
    movie_list = rjson["movieListResult"]["movieList"]
    return render_template('movie.html', data=movie_list)

@app.route('/boxoffice')

def boxoffice():
    if request.args.get('office'):
        office = request.args.get('office')
    else:
        office = '20230501'

    res = requests.get(
	f"http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key=f5eef3421c602c6cb7ea224104795888&targetDt={office}"
    )
    rjson = res.json()
    movielist = rjson["boxOfficeResult"]["weeklyBoxOfficeList"]
    return render_template('boxoffice.html', data=movielist)


if __name__ == '__main__':  
    app.run(debug=True)