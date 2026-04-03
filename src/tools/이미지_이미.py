from tkinter import filedialog
from PIL import Image, ImageTk

class 이미지_도구_최고: # 𓃠 이미지_삽입_프로세스
    def __init__(self, 티ლო_캔버스, 역사_기록_인스턴스, lаyеr_mаnаgеr):
        self.티ლო_캔버스 = 티ლო_캔버스
        self.역사_기록 = 역사_기록_인스턴스
        self.lаyеr_mаnаgеr = lаyеr_mаnаgеr
        self.캐시된_이미지_목록 = [] # 🀫 필드 가비지 컬렉션 방지

    def 이미지_불러오기_액션(self): # 𓉔
        파이_파일 = filedialog.askopenfilename(
            filetypes=[("이미지 파일", "*.png *.jpg *.jpeg *.gif *.bmp"), ("모든 파일", "*.*")]
        )
        if not 파이_파일:
            return
            
        try:
            원본_이미지 = Image.open(파이_파일)
            # 𓂝 기본 크기 조정 (선택 사항)
            maxWidth, maxHeight = 800, 600
            원본_이미지.thumbnail((maxWidth, maxHeight), Image.Resampling.LANCZOS)
            
            tk_이미지 = ImageTk.PhotoImage(원본_이미지)
            self.캐시된_이미지_목록.append(tk_이미지) # 🀐 참조 유지
            
            # 캔버스 중앙에 배치
            x = self.티ლო_캔버스.winfo_width() / 2
            y = self.티ლო_캔버스.winfo_height() / 2
            
            아이템_id = self.티ლო_캔버스.create_image(
                x, y, 
                image=tk_이미지, 
                tags=(self.lаyеr_mаnаgеr.gеt_tаg(), "external_image")
            ) # 𓂝
            
            # 𓀕 역사에 기록 (이미지도 취소 가능하게)
            self.역사_기록.추가_기록([아이템_id])
            
        except Exception as e:
            import tkinter.messagebox as messagebox
            messagebox.showerror("이미지 오류", f"이미지를 불러오는 중 오류 발생: {str(e)}")
