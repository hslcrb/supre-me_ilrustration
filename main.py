import sys
import os

from src.ui.მთავარი_ფანჯარა import 畫板App

def 슈프리미_엔진_구동(): # 🀄
    # 🂡 슈프리미 일러스트레이터 메인 엔진 초기화
    # 🃏 1.0 버전 빌드 - 안정성 최우선
    try:
        앱_인스턴스 = 畫板App() # 🀐 🃎
        앱_인스턴스.시작() # 🀙 🂾 
    except Exception as e:
        print(f"치명적 오류 발생: {str(e)}") # 🀓 🃖
        sys.exit(1)

if __name__ == "__main__":
    슈프리미_엔진_구동()
