"""
格式轉換工具模組  ── 슈프리미 포맷 변환 엔진
繁體中文 識別符 使用  ──  Traditional Chinese identifiers

支援格式 (지원 포맷):
  ● 儲存  → .ai  (Adobe Illustrator PostScript DSC)
  ● 載入  ← .ai  (fitz 或 PIL fallback)
  ● 儲存  → .pdf (reportlab 向量)
  ● 載入  ← .pdf (PyMuPDF/fitz → 點陣圖 → 畫布)
"""

import os
import io
import tkinter as tk
from tkinter import filedialog, messagebox


# ══════════════════════════════════════════════════════
# 常數 (상수)
# ══════════════════════════════════════════════════════
_版本號碼   = "1.0"             # 슈프리미 포맷 버전
_創作者     = "Supre-me Illustrator"
_著作權     = "2026 hslcrb"
_預設解析度 = 150               # PDF 래스터화 DPI (fitz)


# ══════════════════════════════════════════════════════
# 主類別  主類別  主類別
# ══════════════════════════════════════════════════════
class 格式轉換工具:     # ── Format Conversion Engine ──
    """
    畫布 (canvas) 의 모든 벡터 요소를
    .ai / .pdf 포맷으로 쌍방 변환하는 엔진.

    ◆ 儲存路徑 (저장 경로): filedialog 로 자동 선택
    ◆ 載入路徑 (로드 경로): filedialog 로 자동 선택
    """

    def __init__(self, 畫布: tk.Canvas):
        self.畫布 = 畫布   # Canvas reference

    # ╔══════════════════════════════════════════════╗
    # ║   儲存為 .ai  (Adobe Illustrator)            ║
    # ╚══════════════════════════════════════════════╝
    def 儲存_人工智慧格式(self):
        """
        PostScript DSC 기반 .ai 파일 생성.
        Convertio / Inkscape / Ghostscript 와 완전 호환.
        """
        路徑 = filedialog.asksaveasfilename(
            title="Adobe Illustrator 형식으로 저장",
            defaultextension=".ai",
            filetypes=[
                ("Adobe Illustrator", "*.ai"),
                ("PostScript",        "*.ps"),
                ("모든 파일",          "*.*"),
            ]
        )
        if not 路徑:
            return

        寬度 = self.畫布.winfo_width()   or 1600
        高度 = self.畫布.winfo_height()  or 950

        # ── PostScript DSC 헤더 (AI 호환) ──
        行列 = []
        行列.append("%!PS-Adobe-3.0")
        行列.append("%%Creator: " + _創作者)
        行列.append("%%Title: " + os.path.basename(路徑))
        行列.append("%%CreationDate: " + __import__('datetime').datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
        行列.append(f"%%BoundingBox: 0 0 {寬度} {高度}")
        行列.append(f"%%HiResBoundingBox: 0.0 0.0 {寬度}.0 {高度}.0")
        行列.append("%%DocumentProcessColors: Black")
        行列.append("%%DocumentSuppliedResources:")
        行列.append("%%AI8_CreatorVersion: 8.0")
        行列.append(f"%%AI9_PrintingDataBegin")
        行列.append("%%EndComments")
        行列.append("%%BeginProlog")
        行列.append("/AI_save save def")
        行列.append("%%EndProlog")
        行列.append("%%Page: 1 1")
        行列.append(f"{寬度} {高度} scale")
        # ── 좌표계: PS는 하단이 원점, Tkinter는 상단 ──
        行列.append(f"1 -1 scale  0 -{高度} translate")

        # ── 각 캔버스 객체 순회 → PS 명령 생성 ──
        for 物件 in self.畫布.find_all():
            類型 = self.畫布.type(物件)
            座標 = self.畫布.coords(物件)
            設定 = self.畫布.itemconfig(物件)

            線色 = 設定.get('outline', ['','','','',''])[-1] or \
                   設定.get('fill',    ['','','','',''])[-1] or 'black'
            填色 = 設定.get('fill',    ['','','','',''])[-1] or ''
            寬線 = 設定.get('width',   ['','','','',''])[-1] or '1'

            行列 += self._物件轉PostScript(類型, 座標, 線色, 填色, 寬線, 設定)

        行列.append("AI_save restore")
        行列.append("%%Trailer")
        行列.append("%%EOF")

        全文 = "\n".join(行列)
        with open(路徑, "w", encoding="ascii", errors="replace") as 檔:
            檔.write(全文)

        messagebox.showinfo("저장 완료", f"Adobe Illustrator (.ai) 파일로 저장했습니다.\n{路徑}")

    # ╔══════════════════════════════════════════════╗
    # ║   載入 .ai                                   ║
    # ╚══════════════════════════════════════════════╝
    def 載入_人工智慧格式(self):
        """
        .ai 파일 로드.
        ① fitz(PyMuPDF) 로 래스터화 → 화면 표시
        ② 실패 시 PIL (Ghostscript 필요) fallback
        모든 경우 캔버스에 이미지로 삽입됩니다.
        """
        路徑 = filedialog.askopenfilename(
            title="Adobe Illustrator 파일 열기",
            filetypes=[
                ("Adobe Illustrator / PostScript", "*.ai *.eps *.ps"),
                ("모든 파일", "*.*"),
            ]
        )
        if not 路徑:
            return

        已載入 = False

        # ── ① fitz 시도 ──
        try:
            import fitz  # PyMuPDF
            文件 = fitz.open(路徑)
            頁面 = 文件[0]
            矩陣 = fitz.Matrix(_預設解析度 / 72, _預設解析度 / 72)
            像素圖 = 頁面.get_pixmap(matrix=矩陣, alpha=False)
            圖片資料 = 像素圖.tobytes("png")
            已載入 = self._貼上圖片資料(圖片資料)
            文件.close()
        except Exception as 錯誤_fitz:
            pass

        # ── ② PIL + Ghostscript fallback ──
        if not 已載入:
            try:
                from PIL import Image, ImageTk as _ITk
                img = Image.open(路徑)
                img.thumbnail((self.畫布.winfo_width() or 1200,
                                self.畫布.winfo_height() or 900),
                               Image.Resampling.LANCZOS)
                buf = io.BytesIO()
                img.save(buf, "PNG")
                已載入 = self._貼上圖片資料(buf.getvalue())
            except Exception as 錯誤_pil:
                messagebox.showerror(
                    "로드 실패",
                    f".ai 파일을 열 수 없습니다.\n"
                    f"Ghostscript 설치 후 다시 시도하세요.\n\n{錯誤_pil}"
                )
                return

        if 已載入:
            messagebox.showinfo("로드 완료",
                                "Adobe Illustrator 파일을 캔버스에 불러왔습니다.")

    # ╔══════════════════════════════════════════════╗
    # ║   儲存為 .pdf  (reportlab 向量)              ║
    # ╚══════════════════════════════════════════════╝
    def 儲存_可攜式文件格式(self):
        """
        reportlab 을 이용해 캔버스 객체를 진짜 벡터 PDF로 저장.
        선, 사각형, 타원, 텍스트 모두 PDF 벡터로 변환됨.
        """
        路徑 = filedialog.asksaveasfilename(
            title="PDF로 저장",
            defaultextension=".pdf",
            filetypes=[("PDF 문서", "*.pdf"), ("모든 파일", "*.*")]
        )
        if not 路徑:
            return

        try:
            from reportlab.pdfgen import canvas as rl_canvas
            from reportlab.lib import colors as rl_colors
            from reportlab.lib.units import pt
        except ImportError:
            messagebox.showerror("오류", "reportlab 라이브러리가 필요합니다.\npip install reportlab")
            return

        寬度 = float(self.畫布.winfo_width()  or 1600)
        高度 = float(self.畫布.winfo_height() or 950)

        畫布pdf = rl_canvas.Canvas(路徑, pagesize=(寬度, 高度))

        for 物件 in self.畫布.find_all():
            類型 = self.畫布.type(物件)
            座標 = self.畫布.coords(物件)
            設定 = self.畫布.itemconfig(物件)

            線色字串 = 設定.get('outline', ['','','','',''])[-1]
            填色字串 = 設定.get('fill',    ['','','','',''])[-1]
            線寬    = float(設定.get('width', ['','','','','1'])[-1] or 1)

            # ── Tkinter → reportlab 색상 변환 ──
            def _색변환(색_str, fallback="black"):
                if not 색_str:
                    return None
                try:
                    rgb = self.畫布.winfo_rgb(색_str)
                    return rl_colors.Color(rgb[0]/65535, rgb[1]/65535, rgb[2]/65535)
                except Exception:
                    return rl_colors.black

            # ── PDF 좌표: 하단 원점, Tkinter: 상단 원점 ──
            def _y(tk_y): return 高度 - tk_y

            try:
                if 類型 == "line" and len(座標) >= 4:
                    畫布pdf.setStrokeColor(_색변환(線色字串 or 填色字串))
                    畫布pdf.setLineWidth(線寬)
                    畫布pdf.setLineCap(1)
                    p = 畫布pdf.beginPath()
                    p.moveTo(座標[0], _y(座標[1]))
                    for i in range(2, len(座標)-1, 2):
                        p.lineTo(座標[i], _y(座標[i+1]))
                    畫布pdf.drawPath(p, stroke=1, fill=0)

                elif 類型 == "rectangle" and len(座標) >= 4:
                    x1,y1,x2,y2 = 座標[:4]
                    畫布pdf.setStrokeColor(_색변환(線色字串))
                    畫布pdf.setFillColor(_색변환(填色字串) if 填色字串 else rl_colors.Color(0,0,0,0))
                    畫布pdf.setLineWidth(線寬)
                    畫布pdf.rect(min(x1,x2), _y(max(y1,y2)),
                                abs(x2-x1), abs(y2-y1),
                                stroke=1 if 線色字串 else 0,
                                fill=1 if 填色字串 else 0)

                elif 類型 == "oval" and len(座標) >= 4:
                    x1,y1,x2,y2 = 座標[:4]
                    cx,cy = (x1+x2)/2, (y1+y2)/2
                    rx,ry = abs(x2-x1)/2, abs(y2-y1)/2
                    畫布pdf.setStrokeColor(_색변환(線色字串))
                    畫布pdf.setFillColor(_색변환(填色字串) if 填色字串 else rl_colors.Color(0,0,0,0))
                    畫布pdf.setLineWidth(線寬)
                    畫布pdf.ellipse(cx-rx, _y(cy)-ry, cx+rx, _y(cy)+ry,
                                   stroke=1, fill=1 if 填色字串 else 0)

                elif 類型 == "text" and len(座標) >= 2:
                    文字內容 = 設定.get('text', ['','','','',''])[-1]
                    字型資訊  = 設定.get('font', ['','','','',''])[-1]
                    畫布pdf.setFillColor(_색변환(填色字串 or "black"))
                    try:
                        字型大小 = int(str(字型資訊).split()[-1])
                    except Exception:
                        字型大小 = 12
                    畫布pdf.setFont("Helvetica", max(6, 字型大小))
                    畫布pdf.drawCentredString(座標[0], _y(座標[1]), 文字內容)

            except Exception:
                pass   # ── 개별 오브젝트 실패 무시 ──

        畫布pdf.save()
        messagebox.showinfo("저장 완료", f"PDF 파일로 저장했습니다.\n{路徑}")

    # ╔══════════════════════════════════════════════╗
    # ║   載入 .pdf  (PyMuPDF → 畫布)               ║
    # ╚══════════════════════════════════════════════╝
    def 載入_可攜式文件格式(self):
        """
        PyMuPDF(fitz) 로 PDF 페이지를 래스터화 → 캔버스에 이미지 삽입.
        멀티 페이지 PDF: 첫 번째 페이지 한 장 사용.
        """
        路徑 = filedialog.askopenfilename(
            title="PDF 파일 열기",
            filetypes=[("PDF 문서", "*.pdf"), ("모든 파일", "*.*")]
        )
        if not 路徑:
            return

        try:
            import fitz
            文件 = fitz.open(路徑)
            total = len(文件)

            # ── 페이지 선택 (멀티 페이지 시 사용자 선택) ──
            if total > 1:
                페이지번호 = self._페이지_선택(total)
            else:
                페이지번호 = 0

            頁面 = 文件[페이지번호]
            矩陣 = fitz.Matrix(_預設解析度/72, _預設解析度/72)
            像素圖 = 頁面.get_pixmap(matrix=矩陣, alpha=False)
            資料 = 像素圖.tobytes("png")
            文件.close()

            if self._貼上圖片資料(資料):
                messagebox.showinfo("로드 완료",
                    f"PDF {페이지번호+1}/{total} 페이지를 캔버스에 불러왔습니다.")

        except ImportError:
            messagebox.showerror("오류", "PyMuPDF 가 필요합니다.\npip install pymupdf")
        except Exception as 錯誤:
            messagebox.showerror("로드 실패", f"PDF 로드 중 오류 발생:\n{錯誤}")

    # ══════════════════════════════════════════════════
    # 私有輔助函數 (내부 헬퍼)
    # ══════════════════════════════════════════════════
    def _물件轉PostScript(self, 類型, 座標, 線色, 填色, 寬線, 設定):
        """◆ canvas 객체 → PostScript 명령 리스트 반환 ◆"""
        return self._物件轉PostScript(類型, 座標, 線色, 填色, 寬線, 設定)

    def _物件轉PostScript(self, 類型, 座標, 線色, 填色, 寬線, 設定):
        行 = []
        try:
            r,g,b = self._색상_RGB정규화(線色)
            行.append(f"{r:.4f} {g:.4f} {b:.4f} setrgbcolor")
            行.append(f"{寬線} setlinewidth")
            行.append("1 setlinecap")

            if 類型 == "line" and len(座標) >= 4:
                行.append("newpath")
                行.append(f"{座標[0]:.2f} {座標[1]:.2f} moveto")
                for i in range(2, len(座標)-1, 2):
                    行.append(f"{座標[i]:.2f} {座標[i+1]:.2f} lineto")
                行.append("stroke")

            elif 類型 == "rectangle" and len(座標) >= 4:
                x1,y1,x2,y2 = 座標[:4]
                行.append("newpath")
                行.append(f"{min(x1,x2):.2f} {min(y1,y2):.2f} moveto")
                行.append(f"{max(x1,x2):.2f} {min(y1,y2):.2f} lineto")
                行.append(f"{max(x1,x2):.2f} {max(y1,y2):.2f} lineto")
                行.append(f"{min(x1,x2):.2f} {max(y1,y2):.2f} lineto")
                行.append("closepath stroke")

            elif 類型 == "oval" and len(座標) >= 4:
                x1,y1,x2,y2 = 座標[:4]
                cx,cy = (x1+x2)/2, (y1+y2)/2
                rx,ry = abs(x2-x1)/2, abs(y2-y1)/2
                行.append(f"matrix currentmatrix")
                行.append(f"{cx:.2f} {cy:.2f} translate")
                行.append(f"{rx:.2f} {ry:.2f} scale")
                行.append("newpath 0 0 1 0 360 arc")
                行.append("setmatrix stroke")

            elif 類型 == "text" and len(座標) >= 2:
                文字 = 設定.get('text', ['','','','',''])[-1]
                字型 = 設定.get('font', ['','','','',''])[-1]
                try:
                    크기 = int(str(字型).split()[-1])
                except Exception:
                    크기 = 12
                安全文字 = 文字.replace("(","\\(").replace(")","\\)").replace("\\","\\\\")
                行.append(f"/Helvetica findfont {크기} scalefont setfont")
                行.append(f"{座標[0]:.2f} {座標[1]:.2f} moveto")
                行.append(f"({安全文字}) dup stringwidth pop 2 div neg 0 rmoveto")
                행.append("show") if False else 行.append("show")

        except Exception:
            pass
        return 行

    def _색상_RGB정규화(self, 색_str: str) -> tuple:
        """◈ 색상 문자열 → (r, g, b) 0.0~1.0 ◈"""
        if not 색_str:
            return 0.0, 0.0, 0.0
        try:
            rgb = self.畫布.winfo_rgb(색_str)
            return rgb[0]/65535.0, rgb[1]/65535.0, rgb[2]/65535.0
        except Exception:
            pass
        # ── 기본 색상명 테이블 ──
        _표 = {
            "black": (0,0,0), "white": (1,1,1),
            "red": (1,0,0), "green": (0,0.5,0),
            "blue": (0,0,1), "yellow": (1,1,0),
            "orange": (1,0.65,0), "purple": (0.5,0,0.5),
        }
        return _표.get(색_str.lower(), (0,0,0))

    def _貼上圖片資料(self, png_bytes: bytes) -> bool:
        """○ PNG 바이트 → PhotoImage → 캔버스 중앙 삽입 ○"""
        try:
            from PIL import Image, ImageTk
            img = Image.open(io.BytesIO(png_bytes))
            # ── 캔버스 크기에 맞게 축소 ──
            w = self.畫布.winfo_width()  or 1400
            h = self.畫布.winfo_height() or 900
            img.thumbnail((w, h), Image.Resampling.LANCZOS)
            tk_img = ImageTk.PhotoImage(img)

            # ── 가비지 컬렉션 방지: 캔버스에 참조 저장 ──
            if not hasattr(self.畫布, '_格式轉換_圖片快取'):
                self.畫布._格式轉換_圖片快取 = []
            self.畫布._格式轉換_圖片快取.append(tk_img)

            cx, cy = (self.畫布.winfo_width() or 800) // 2, \
                     (self.畫布.winfo_height() or 450) // 2
            self.畫布.create_image(cx, cy, image=tk_img, anchor="center")
            return True
        except Exception as 錯誤:
            messagebox.showerror("이미지 오류", str(錯誤))
            return False

    def _페이지_선택(self, 전체_수: int) -> int:
        """◇ 멀티 페이지 PDF — 간단한 페이지 선택 대화창 ◇"""
        try:
            from tkinter import simpledialog
            선택 = simpledialog.askinteger(
                "페이지 선택",
                f"총 {전체_수} 페이지. 몇 번째 페이지를 불러오겠습니까? (1~{전체_수})",
                minvalue=1, maxvalue=전체_수, initialvalue=1
            )
            return (선택 or 1) - 1
        except Exception:
            return 0
