문제 1번
게임 중 입력하는 숫자에 따라 입력가능한 범위가 바뀌게 변경하였습니다.

문제 2번
요구사항을 완성한 기본파일과
class형식으로 바꿔본 class파일을 따로 두었습니다
이유는 class파일의 경우 다중if문을 사용하라는 문제의 요구에 맞지 않는 부분이 있었기 때문입니다.

문제 3번
요구사항을 완성한 기본파일과
추가기능을 더한 class파일을 따로 두었습니다.
이유는 class파일의 경우 로그인 기능을 따로 만들어서, 멤버생성 - 로그인 과정을 거치면
이후 로그인 상태를 확인하고 로그아웃/회원탈퇴/글작성(작성자:로그인중인 username), 글삭제(로그인중인 user가 작성자한 글만 가능),
글 검색(제목, 내용, 작성자)기능을 추가하였습니다.

문제 4번
파일 3종(sqlite, sqlalchemy,session)이 있습니다.
 - sqlite 는 DB에서 계산한 후 데이터를 받아왔습니다. + rps_game, rps_game_result.html
 - sqlalchemy는 배운것처럼 작성하였습니다. + rps_game_01.html
 - session은 기존 게임의 기록이 초기화되는 문제로 도입하고 만들어 보았는데,
    browser가 꺼지면 count와 db의 기록이 조금 맞지 않는 문제가 있습니다. + rps_game_02.html
