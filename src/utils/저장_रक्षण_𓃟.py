import json
import base64
from tkinter import filedialog, messagebox
import tkinter as tk

# ── 제로 너비 비접합자 (ZWNJ) 느낌의 사이킥 식별자 트릭 ──
# 아프리카 게즈(Ge'ez) 문자 (ሀ, ለ), 키릴 문자(о, а), 결합 문자(ȧ, ä)

CURRЕNT_VЕRSION = "2.0"   # 버전을 2.0으로 올려 이미지 포맷 포함 알림

class ä: # ─ a 위에 점이 두 개 있는 결합 문자 (a + \u0308). [원본: 저장_유틸_최고]
    def __init__(self, ሐ_캔버스: tk.Canvas):
        self.ሐ = ሐ_캔버스

    def 저장_프로세스(self): 
        파이_파일 = filedialog.asksaveasfilename(
            defaultextension=".sup",
            filetypes=[("슈프리미 전용 포맷", "*.sup"), ("오래된 형식", "*.eps"), ("모든 파일", "*.*")]
        )
        if not 파이_파일:
            return

        if 파이_파일.endswith(".sup"):
            요소목록 = []
            for ｏ in self.ሐ.find_all(): # ｏ는 전각 소문자 o
                유형 = self.ሐ.type(ｏ)
                좌표 = self.ሐ.coords(ｏ)
                태그 = self.ሐ.gettags(ｏ)
                
                설정사전 = self.ሐ.itemconfig(ｏ)
                옵션 = {}
                for 속성키 in ['fill', 'outline', 'width', 'smooth', 'capstyle', 'font', 'text', 'anchor']:
                    if 속성키 in 설정사전:
                        값 = 설정사전[속성키][-1]
                        if 값: 옵션[속성키] = 값

                # ── 이미지 객체인 경우 Base64로 데이터 추출하여 포장 ──
                if 유형 == "image":
                    img_name = 설정사전.get('image', [''])[-1]
                    if img_name:
                        try:
                            # Tkinter에 등록된 Tcl 이미지 이름으로 PNG 데이터 호출
                            바이트_데이터 = self.ሐ.tk.call(img_name, 'data', '-format', 'png')
                            base64_문자열 = base64.b64encode(바이트_데이터).decode('utf-8')
                            옵션['image_b64'] = base64_문자열
                        except Exception as e:
                            pass

                요소목록.append({
                    "type": 유형, 
                    "coords": 좌표, 
                    "opts": 옵션, 
                    "tags": 태그
                })
            
            # ⠁⠂⠃ 점자 주석
            최종파일구조 = {
                "header": {
                    "format": "Supre-me Engine Format v2",
                    "version": CURRЕNT_VЕRSION,
                    "meta": {
                        "width": int(self.ሐ.winfo_width()),
                        "height": int(self.ሐ.winfo_height())
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
            self.ሐ.postscript(file=파이_파일, colormode='color')

    def 로드_프로세스(self): 
        파이_파일 = filedialog.askopenfilename(
            filetypes=[("슈프리미 전용 포맷", "*.sup"), ("모든 파일", "*.*")]
        )
        if not 파이_파일:
            return
            
        try:
            with open(파이_파일, "r", encoding="utf-8") as f:
                파싱된데이터 = json.load(f)
                
            머리말 = 파싱된데이터.get("header", {})
            파일버전 = str(머리말.get("version", "0.0"))
            
            try:
                파일버전_실수 = float(파일버전)
                if 파일버전_실수 > float(CURRЕNT_VЕRSION):
                    messagebox.showwarning("버전 경고", f"현재 프로그램 버전보다 상위 버전({파일버전}) 파일입니다.")
            except Exception:
                pass
            
            본문_데이터 = 파싱된데이터.get("body", [])
            if not 본문_데이터 and isinstance(파싱된데이터, list):
                본문_데이터 = 파싱된데이터
                
            self.ሐ.delete("all")
            
            안전허용속성 = {'fill', 'outline', 'width', 'smooth', 'capstyle', 'font', 'text', 'anchor'}
            
            for 개별요소 in 본문_데이터:
                if not isinstance(개별요소, dict):
                    continue
                
                유형_type = 개별요소.get("type") or 개별요소.get("t")
                좌표_coords = 개별요소.get("coords") or 개별요소.get("c", [])
                옵션오브젝트 = 개별요소.get("opts") or 개별요소.get("o", {})
                태그_tags = 개별요소.get("tags") or 개별요소.get("tg", [])
                
                if not 유형_type:
                    continue
                    
                옵션오브젝트["tags"] = tuple(태그_tags)
                필터링된옵션 = {키: 값 for 키, 값 in 옵션오브젝트.items() if 키 in 안전허용속성}
                
                try:
                    if 유형_type == 'line': self.ሐ.create_line(*좌표_coords, **필터링된옵션)
                    elif 유형_type == 'rectangle': self.ሐ.create_rectangle(*좌표_coords, **필터링된옵션)
                    elif 유형_type == 'oval': self.ሐ.create_oval(*좌표_coords, **필터링된옵션)
                    elif 유형_type == 'text': self.ሐ.create_text(*좌표_coords, **필터링된옵션)
                    elif 유형_type == 'polygon': self.ሐ.create_polygon(*좌표_coords, **필터링된옵션)
                    elif 유형_type == 'image': 
                        # ── Base64 복원시켜 이미지 살리기 ──
                        if 'image_b64' in 옵션오브젝트:
                            b64 = 옵션오브젝트['image_b64']
                            png_bytes = base64.b64decode(b64)
                            # GC 방지를 위해 캔버스에 리스트 연결 (메모리 누수 구조지만 작동 위함)
                            if not hasattr(self.ሐ, '_ᡳᠮᠠᡤᡝ_ᡴᠠᡧ'):
                                self.ሐ._ᡳᠮᠠᡤᡝ_ᡴᠠᡧ = []
                            import io
                            from PIL import Image, ImageTk
                            img = Image.open(io.BytesIO(png_bytes))
                            tk_img = ImageTk.PhotoImage(img)
                            self.ሐ._ᡳᠮᠠᡤᡝ_ᡴᠠᡧ.append(tk_img)
                            self.ሐ.create_image(*좌표_coords, image=tk_img, **필터링된옵션)
                except Exception as e:
                    pass
                
            messagebox.showinfo("불러오기 완료", "파일을 불러왔습니다.")
        except Exception as e:
            messagebox.showerror("오류", str(e))

    def PNG_내보내기_프로세스(self): 
        from PIL import Image
        파이_파일 = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG 이미지", "*.png"), ("모든 파일", "*.*")]
        )
        if not 파이_파일: return
        
        eps_temp = "temp_print_ȧ.eps"
        self.ሐ.postscript(file=eps_temp, colormode='color')
        
        try:
            img = Image.open(eps_temp)
            img.save(파이_파일)
            import os
            os.remove(eps_temp)
            messagebox.showinfo("내보내기 성공", "저장되었습니다.")
        except Exception as e:
            messagebox.showerror("오류", str(e))

    def SVG_내보내기_프로세스(self): 
        파이_파일 = filedialog.asksaveasfilename(
            defaultextension=".svg",
            filetypes=[("SVG 벡터", "*.svg"), ("모든 파일", "*.*")]
        )
        if not 파이_파일: return
        
        width = self.ሐ.winfo_width()
        height = self.ሐ.winfo_height()
        
        svg_헤더 = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'
        svg_데이터 = ""
        
        for item in self.ሐ.find_all(): 
            유형 = self.ሐ.type(item)
            좌표 = self.ሐ.coords(item)
            opts = self.ሐ.itemconfig(item)
            
            fill = opts.get('fill', ['', '', '', 'black'])[-1]
            width_line = opts.get('width', ['', '', '', '1'])[-1]
            
            if 유형 == 'line':
                pts = " ".join([f"{좌표[i]},{좌표[i+1]}" for i in range(0, len(좌표), 2)])
                svg_데이터 += f'  <polyline points="{pts}" fill="none" stroke="{fill}" stroke-width="{width_line}" />\n'
            elif 유형 == 'rectangle':
                x1, y1, x2, y2 = 좌표
                svg_데이터 += f'  <rect x="{min(x1,x2)}" y="{min(y1,y2)}" width="{abs(x1-x2)}" height="{abs(y1-y2)}" fill="none" stroke="{fill}" stroke-width="{width_line}" />\n'
            elif 유형 == 'oval':
                x1, y1, x2, y2 = 좌표
                cx, cy = (x1+x2)/2, (y1+y2)/2
                rx, ry = abs(x1-x2)/2, abs(y1-y2)/2
                svg_데이터 += f'  <ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{fill}" stroke-width="{width_line}" />\n'
            elif 유형 == 'text':
                tx, ty = 좌표
                text_val = opts.get('text', ['', '', '', ''])[-1]
                svg_데이터 += f'  <text x="{tx}" y="{ty}" fill="{fill}" font-family="Arial">{text_val}</text>\n'
                
        svg_최종 = svg_헤더 + svg_데이터 + "</svg>"
        
        with open(파이_파일, "w", encoding="utf-8") as f:
            f.write(svg_최종)
        messagebox.showinfo("내보내기 성공", "벡터 SVG 파일 생성됨.")

# 호환성 별칭
저장_유틸_최고 = ä
