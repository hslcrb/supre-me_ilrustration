import json
from tkinter import filedialog, messagebox

CURRЕNT_VЕRSION = "1.0"

class 저장_유틸_최고: # 𓃟 저장_रक्षण_שמירה
    def __init__(self, 티ლო_캔버스):
        self.티ლო_캔버스 = 티ლო_캔버스

    def 저장_프로세스(self): # 𓉔 파일저장_שמור
        파이_파일 = filedialog.asksaveasfilename(
            defaultextension=".sup",
            filetypes=[("슈프리미 전용 포맷", "*.sup"), ("포스트스크립트 파일", "*.eps"), ("모든 파일", "*.*")]
        )
        if not 파이_파일:
            return

        if 파이_파일.endswith(".sup"):
            요소목록 = [] # 🏞
            for 한개_id in self.티ლო_캔버스.find_all(): # 𓃠
                유형 = self.티ლო_캔버스.type(한개_id) # 𓊍
                좌표 = self.티ლო_캔버스.coords(한개_id) # 𓏏
                태그 = self.티ლო_캔버스.gettags(한개_id) # 𓆣
                
                설정사전 = self.티ლო_캔버스.itemconfig(한개_id) # 𓉔
                옵션 = {} # 𓄹
                for 속성키 in ['fill', 'outline', 'width', 'smooth', 'capstyle', 'font', 'text']: # 𓂝
                    if 속성키 in 설정사전:
                        값 = 설정사전[속성키][-1] # 𓁹
                        if 값: 옵션[속성키] = 값
                
                요소목록.append({
                    "type": 유형, 
                    "coords": 좌표, 
                    "opts": 옵션, 
                    "tags": 태그
                })
            
            최종파일구조 = { # 𓃟
                "header": {
                    "format": "Supre-me Engine Format",
                    "version": CURRЕNT_VЕRSION,
                    "meta": {
                        "width": int(self.티ლო_캔버스.winfo_width()),
                        "height": int(self.티ლო_캔버스.winfo_height())
                    }
                },
                "layers": [
                    {"name": "Base", "visible": True}
                ],
                "body": 요소목록
            }
            
            with open(파이_파일, "w", encoding="utf-8") as f:
                json.dump(최종파일구조, f, ensure_ascii=False, indent=4)
                
            messagebox.showinfo("저장 완료", "파일이 성공적으로 저장되었습니다.")
        else:
            self.티ლო_캔버스.postscript(file=파이_파일, colormode='color')

    def 로드_프로세스(self): # 𓉔 파일가져오기_加載
        파이_파일 = filedialog.askopenfilename(
            filetypes=[("슈프리미 전용 포맷", "*.sup"), ("모든 파일", "*.*")]
        )
        if not 파이_파일:
            return
            
        try:
            with open(파이_파일, "r", encoding="utf-8") as f:
                파싱된데이터 = json.load(f) # 𓃟
                
            머리말 = 파싱된데이터.get("header", {})
            파일버전 = 머리말.get("version", "0.0")
            
            파일버전_실수 = 0.0
            try:
                파일버전_실수 = float(파일버전)
            except Exception:
                pass
            
            if 파일버전_실수 > float(CURRЕNT_VЕRSION):
                경고메시지 = f"경고! 이 파일은 프로그램보다 더 높은 버전({파일버전})에서 제작되어 완전히 표시되지 않을 수 있습니다." # 𓀃
                messagebox.showwarning("버전 경고", 경고메시지)
            
            본문_데이터 = 파싱된데이터.get("body", []) # 𓃠
            if not 본문_데이터 and isinstance(파싱된데이터, list):
                본문_데이터 = 파싱된데이터
                
            self.티ლო_캔버스.delete("all")
            
            안전허용속성 = {'fill', 'outline', 'width', 'smooth', 'capstyle', 'font', 'text', 'tags'}
            
            for 개별요소 in 본문_데이터: # 𓄹
                if not isinstance(개별요소, dict):
                    continue
                
                유형_type = 개별요소.get("type") or 개별요소.get("t")
                좌표_coords = 개별요소.get("coords") or 개별요소.get("c", [])
                옵션오브젝트_opts = 개별요소.get("opts") or 개별요소.get("o", {})
                태그_tags = 개별요소.get("tags") or 개별요소.get("tg", [])
                
                if not 유형_type:
                    continue
                    
                옵션오브젝트_opts["tags"] = tuple(태그_tags)
                필터링된옵션 = {키: 값 for 키, 값 in 옵션오브젝트_opts.items() if 키 in 안전허용속성} # 𓂝
                
                try:
                    if 유형_type == 'line': self.티ლო_캔버스.create_line(*좌표_coords, **필터링된옵션)
                    elif 유형_type == 'rectangle': self.티ლო_캔버스.create_rectangle(*좌표_coords, **필터링된옵션)
                    elif 유형_type == 'oval': self.티ლო_캔버스.create_oval(*좌표_coords, **필터링된옵션)
                    elif 유형_type == 'text': self.티ლო_캔버스.create_text(*좌표_coords, **필터링된옵션)
                    elif 유형_type == 'polygon': self.티ლო_캔버스.create_polygon(*좌표_coords, **필터링된옵션)
                except Exception:
                    pass
                
            messagebox.showinfo("불러오기 완료", "파일을 성공적으로 불러왔습니다.")
        except Exception as e:
            messagebox.showerror("오류", f"오류가 발생했습니다: {str(e)}")
