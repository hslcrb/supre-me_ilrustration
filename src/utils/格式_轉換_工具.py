"""
ᡤᡳᠰᡠᠨ ᡥᡝᡵᡤᡝᠨ ᠠᡤᡡᡵᠠ — 格式轉換工具 v2.0
ᠮᠠᠨᠵᡠ ᡤᡳᠰᡠᠨ ᡝ ᠠᡤᡡᡵᠠ  (Manchu-script Format Engine)

ᡤᡝᠮᡠᠯᡝ:   save / 儲存
ᡤᠠᠵᡳ:    load / 載入
ᡥᡝᡵᡤᡝᠨ: format / 格式

Ghostscript: C:\\Program Files\\gs\\gs10.07.0\\bin\\gswin64c.exe
reportlab  : pip 설치됨
PyMuPDF    : pip 설치됨
"""

import os
import io
import glob
import tempfile
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox


# ══════════════════════════════════════════════════════
# ᡥᡝᡵᡤᡝᠨ ᡳᠴᡳ ─ Constants / 常數
# ══════════════════════════════════════════════════════

# Ghostscript 실행 파일 경로 자동 탐색
def _ᡤᠰ_ᠵᡠᡵᡤᠠᠨ() -> str:  # gs_find
    """ᡤᠰ ᠪᠠ ᠪᡠᠯᡠᠮᠪᡳ — Ghostscript 경로 탐색 및 보안 검증"""
    candidates = ["gswin64c", "gswin32c", "gs"]
    
    # Windows 설치 경로 탐색 패턴 추가
    patterns = [
        r"C:\Program Files\gs\gs*\bin\gswin64c.exe",
        r"C:\Program Files\gs\gs*\bin\gswin32c.exe",
    ]
    for pat in patterns:
        hits = sorted(glob.glob(pat), reverse=True)
        candidates.extend(hits)

    for cmd in candidates:
        try:
            # ꧄ 실행 전 버전 정보를 확인하여 실제 Ghostscript인지 검증 (Security)
            r = subprocess.run([cmd, "-version"], capture_output=True, text=True, timeout=2)
            if r.returncode == 0 and "Ghostscript" in r.stdout:
                return cmd
        except: pass
    return ""


_ᡤᠰ_ᠵᡠᡵᡤᡝᠨ   = _ᡤᠰ_ᠵᡠᡵᡤᠠᠨ()   # ᡤᠰ ᡝᠵᡝᠨ — GS executable path
_ᡤᠰ_ᠪᡳ_ᡝ     = bool(_ᡤᠰ_ᠵᡠᡵᡤᡝᠨ)  # ᡤᠰ ᠪᡳ ─ GS available?
_ᡩᠣᠰᡳ_ᡳᠯᡝᡨᡠᠨ = 150               # ᡩᠣᠰᡳ — DPI resolution
_ᡠᡵᡝ_ᡤᡝᠨ     = "Supre-me Illustrator v2.1"


# ══════════════════════════════════════════════════════
# ᡧᡠ ᡴᡡᠪᡠᠯᡝᠨ — Main Class / 主類別
# ══════════════════════════════════════════════════════
class 格式轉換工具:    # ᡤᡳᠰᡠᠨ ᡥᡝᡵᡤᡝᠨ ᠠᡤᡡᡵᠠ — Format Conversion Engine
    """
    ᡤᡝᠮᡠᠯᡝᠮᠪᡳ ᡝᠮᡝ ᡤᠠᠵᡳᠮᠪᡳ — Save & Load Engine

    .ai  ─ 儲存 : reportlab PDF → AI DSC 헤더 주입 → 진짜 .ai
    .ai  ─ 載入 : Ghostscript 래스터화 → 캔버스
    .pdf ─ 儲存 : reportlab 벡터 PDF
    .pdf ─ 載入 : PyMuPDF(fitz) 래스터화 → 캔버스
    """

    def __init__(self, ᡥᡡᠸᠠᠨ: tk.Canvas):
        # ᡥᡡᠸᠠᠨ = 畫布 = Canvas
        self.ᡥᡡᠸᠠᠨ = ᡥᡡᠸᠠᠨ

    # ╔══════════════════════════════════════════════╗
    # ║  儲存為 .ai  ─  ᡥᡝᡵᡤᡝᠨ ᡤᡝᠮᡠᠯᡝ               ║
    # ╚══════════════════════════════════════════════╝
    def 儲存_人工智慧格式(self):
        """
        ᡠᡵᡝᠮᡠᡨ ── AI 파일 저장 전략:
        1. reportlab 으로 진짜 PDF 생성
        2. AI DSC 호환 헤더를 파일 앞에 삽입
        3. .ai 확장자로 저장
        → Adobe Illustrator CS4+ / Inkscape / Convertio 모두 열 수 있음
        """
        ᠵᡠᡵᡤᠠᠨ = filedialog.asksaveasfilename(   # ᠵᡠᡵᡤᠠᠨ = path
            title="Adobe Illustrator (.ai) 형식으로 저장",
            defaultextension=".ai",
            filetypes=[
                ("Adobe Illustrator", "*.ai"),
                ("모든 파일",          "*.*"),
            ]
        )
        if not ᠵᡠᡵᡤᠠᠨ:
            return

        try:
            from reportlab.pdfgen import canvas as rl_canvas
            from reportlab.lib import colors as rl_colors
        except ImportError:
            messagebox.showerror("오류", "pip install reportlab")
            return

        ᠴᠣᡴᡡᠨ = float(self.ᡥᡡᠸᠠᠨ.winfo_width()  or 1600)  # ᠴᠣᡴᡡᠨ = width
        ᡩᡝᡵᡤᡳ = float(self.ᡥᡡᠸᠠᠨ.winfo_height() or 950)   # ᡩᡝᡵᡤᡳ = height

        # ── PDF를 메모리 버퍼에 생성 ──
        ᠪᡠᡶᡝᡵ = io.BytesIO()   # ᠪᡠᡶᡝᡵ = buffer
        ᠪᡡᡴᡡ  = rl_canvas.Canvas(ᠪᡠᡶᡝᡵ, pagesize=(ᠴᠣᡴᡡᠨ, ᡩᡝᡵᡤᡳ))
        self._ᡴᠠᠨᡳᠪᠠᠰᠠ_ᡤᡝᠮᡠᠯᡝ(ᠪᡡᡴᡡ, ᠴᠣᡴᡡᠨ, ᡩᡝᡵᡤᡳ, rl_colors)   # 캔버스 객체 → PDF
        ᠪᡡᡴᡡ.save()
        ᠫᡩᡶ_ᡩᠠᡨᠠ = ᠪᡠᡶᡝᡵ.getvalue()

        # ── Adobe Illustrator 호환 DSC 헤더 주입 ──
        # 핵심: PDF 앞에 AI 메타 주석을 붙이면 Illustrator가 인식
        import datetime
        ᡩᠣᠸᠠ = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

        ᡥᡝᠠᡩᡝᡵ = (
            f"%!PS-Adobe-3.0\n"
            f"%%Creator: {_ᡠᡵᡝ_ᡤᡝᠨ}\n"
            f"%%Title: {os.path.basename(ᠵᡠᡵᡤᠠᠨ)}\n"
            f"%%CreationDate: {ᡩᠣᠸᠠ}\n"
            f"%%BoundingBox: 0 0 {int(ᠴᠣᡴᡡᠨ)} {int(ᡩᡝᡵᡤᡳ)}\n"
            f"%%HiResBoundingBox: 0.000 0.000 {ᠴᠣᡴᡡᠨ:.3f} {ᡩᡝᡵᡤᡳ:.3f}\n"
            f"%%DocumentProcessColors: Cyan Magenta Yellow Black\n"
            f"%%DocumentSuppliedResources:\n"
            f"%%AI8_CreatorVersion: 16.0.0\n"
            f"%%AI9_PrintingDataBegin\n"
            f"%%EndComments\n"
            f"%%BeginProlog\n"
            f"%%EndProlog\n"
            f"%%Page: 1 1\n"
        ).encode("ascii")

        ᡶᡡᡩᡶᡝᡵ = b"\n%%Trailer\n%%EOF\n"

        # AI 파일 = DSC헤더 + PDF바이너리 + 푸터
        with open(ᠵᡠᡵᡤᠠᠨ, "wb") as ᡶᠠᡭ:   # ᡶᠠᡭ = file
            ᡶᠠᡭ.write(ᡥᡝᠠᡩᡝᡵ)
            ᡶᠠᡭ.write(ᠫᡩᡶ_ᡩᠠᡨᠠ)
            ᡶᠠᡭ.write(ᡶᡡᡩᡶᡝᡵ)

        messagebox.showinfo("저장 완료 ᡤᡝᠮᡠᠯᡝ",
                            f"Adobe Illustrator (.ai) 파일을 저장했습니다:\n{ᠵᡠᡵᡤᠠᠨ}\n\n"
                            f"Illustrator CS4+ / Inkscape / Convertio 에서 열 수 있습니다.")

    # ╔══════════════════════════════════════════════╗
    # ║  載入 .ai  ─  ᡥᡝᡵᡤᡝᠨ ᡤᠠᠵᡳ                  ║
    # ╚══════════════════════════════════════════════╝
    def 載入_人工智慧格式(self):
        self._ㅤレمラيㅤ(filedialog.askopenfilename(title="Adobe AI/EPS", filetypes=[("AI/EPS", "*.ai *.eps *.ps"), ("모든 파일", "*.*")]))

    def 載入_可攜式文件格式(self):
        self._ㅤレمラيㅤ(filedialog.askopenfilename(title="PDF 열기", filetypes=[("PDF文書", "*.pdf"), ("모든 파일", "*.*")]))

    def 儲存_可攜式文件格式(self):
        # ᄠᅳᆮ : 그림을 종이 문서의 형태로 굳히ᄂᆞᆫ 것이ᄅ라. (寫眞 PDF 變換)
        ㅤパيثㅤ = filedialog.asksaveasfilename(title="PDF로 저장", defaultextension=".pdf", filetypes=[("PDF 문서", "*.pdf"), ("모든 파일", "*.*")])
        if not ㅤパيثㅤ: return
        try:
            from reportlab.pdfgen import canvas as rl_canvas
            from reportlab.lib import colors as rl_colors
        except ImportError:
            messagebox.showerror("오류", "pip install reportlab")
            return
        
        ㅤエキسㅤ = float(self.ᡥᡡᠸᠠᠨ.winfo_width() or 1600)
        ㅤワイㅤ = float(self.ᡥᡡᠸᠠᠨ.winfo_height() or 950)
        ㅤホンشㅤ = rl_canvas.Canvas(ㅤパيثㅤ, pagesize=(ㅤエキسㅤ, ㅤワイㅤ))
        self._ᡴᠠᠨᡳᠪᠠᠰᠠ_ᡤᡝᠮᡠᠯᡝ(ㅤホンشㅤ, ㅤエキسㅤ, ㅤワイㅤ, rl_colors)
        ㅤホンشㅤ.save()
        messagebox.showinfo("저장 완료 ᡤᡝᠮᡠᠯᡝ", f"PDF 파일을 저장했습니다:\n{ㅤパيثㅤ}")
    def SVG_불러오기_프로세스(self):
        # ᄠᅳᆮ : 순수ᄒᆞᆫ SVG 문서를 들여와 붓질로 살려내ᄂᆞᆫ다.
        self._ㅤレمラيㅤ(filedialog.askopenfilename(title="SVG 열기", filetypes=[("SVG文書", "*.svg"), ("모든 파일", "*.*")]), ㅤイラزㅤ=True)

    def _ㅤレمラيㅤ(self, ㅤパيثㅤ, ㅤイラزㅤ=False):
        # ᄠᅳᆮ : 모든 선(Vector)을 찍어내ᄂᆞᆫ 마법의 용광로이ᄅ라. (Universal Vector Parser)
        # We parse the XML runes & extract the pure paths of the ancients.
        if not ㅤパيثㅤ: return
        import re, base64, io
        from xml.etree import ElementTree as ET
        from PIL import Image, ImageTk

        try:
            if ㅤイラزㅤ:
                with open(ㅤパيثㅤ, "r", encoding="utf-8") as ㅤفァイㅤ:
                    ㅤサنシㅤ = ㅤفァイㅤ.read()
            else:
                import fitz
                ㅤرクンㅤ = fitz.open(ㅤパيثㅤ)
                ㅤホンشㅤ = ㅤرクンㅤ[0]
                ㅤサنシㅤ = ㅤホンشㅤ.get_svg_image()
                if isinstance(ㅤサنシㅤ, bytes): ㅤサنシㅤ = ㅤサنシㅤ.decode('utf-8')
                ㅤرクンㅤ.close()

            ㅤルーテㅤ = re.sub(r'xmlns="[^"]+"', '', ㅤサنシㅤ, count=1)
            ㅤメネジㅤ = ET.fromstring(ㅤルーテㅤ)

            def _ㅤトカシㅤ(ㅤノドرㅤ):
                ㅤタグエㅤ = ㅤノドرㅤ.tag.split('}')[-1]
                ㅤフイلㅤ = ㅤノドرㅤ.attrib.get('fill', 'none')
                if ㅤフイلㅤ == 'none': ㅤフイلㅤ = ''
                ㅤストคㅤ = ㅤノドرㅤ.attrib.get('stroke', 'black')
                ㅤワيトㅤ = float(ㅤノドرㅤ.attrib.get('stroke-width', '1.0'))

                if ㅤタグエㅤ == 'path' or ㅤタグエㅤ == 'polyline' or ㅤタグエㅤ == 'polygon':
                    ㅤデيタㅤ = ㅤノドرㅤ.attrib.get('d', ㅤノドرㅤ.attrib.get('points', ''))
                    ㅤコドسㅤ = list(map(float, re.findall(r'[-+]?[0-9]*\.?[0-9]+', ㅤデيタㅤ)))
                    if len(ㅤコドسㅤ) >= 4:
                        if ㅤフイلㅤ != '':
                            self.ᡥᡡᠸᠠᠨ.create_polygon(*ㅤコドسㅤ, fill=ㅤフイلㅤ, outline=ㅤストคㅤ, width=ㅤワيトㅤ, tags="VECTOR_PATH")
                        else:
                            self.ᡥᡡᠸᠠᠨ.create_line(*ㅤコドسㅤ, fill=ㅤストคㅤ, width=ㅤワيトㅤ, smooth=False, capstyle=tk.ROUND, joinstyle=tk.ROUND, tags="VECTOR_PATH")
                            
                elif ㅤタグエㅤ == 'rect':
                    ㅤエキسㅤ, ㅤワイㅤ = float(ㅤノドرㅤ.attrib.get('x', '0')), float(ㅤノドرㅤ.attrib.get('y', '0'))
                    ㅤウيダㅤ, ㅤハيトㅤ = float(ㅤノドرㅤ.attrib.get('width', '0')), float(ㅤノドرㅤ.attrib.get('height', '0'))
                    self.ᡥᡡᠸᠠᠨ.create_rectangle(ㅤエキسㅤ, ㅤワイㅤ, ㅤエキسㅤ+ㅤウيダㅤ, ㅤワイㅤ+ㅤハيトㅤ, fill=ㅤフイلㅤ, outline=ㅤストคㅤ, width=ㅤワيトㅤ, tags="VECTOR_PATH")
                    
                elif ㅤタグエㅤ == 'image':
                    ㅤヒレفㅤ = ㅤノドرㅤ.attrib.get('href', ㅤノドرㅤ.attrib.get('{http://www.w3.org/1999/xlink}href', ''))
                    if ㅤヒレفㅤ.startswith('data:image'):
                        ㅤマيスㅤ = ㅤヒレفㅤ.split(',')[1]
                        ㅤピルاㅤ = Image.open(io.BytesIO(base64.b64decode(ㅤマيスㅤ)))
                        ㅤテケiㅤ = ImageTk.PhotoImage(ㅤピルاㅤ)
                        if not hasattr(self.ᡥᡡᠸᠠᠨ, 'ㅤ_img_cache'): self.ᡥᡡᠸᠠᠨ.ㅤ_img_cache = []
                        self.ᡥᡡᠸᠠᠨ.ㅤ_img_cache.append(ㅤテケiㅤ)
                        ㅤエキسㅤ, ㅤワイㅤ = float(ㅤノドرㅤ.attrib.get('x', '0')), float(ㅤノドرㅤ.attrib.get('y', '0'))
                        ㅤウيタㅤ = self.ᡥᡡᠸᠠᠨ.create_image(ㅤエキسㅤ, ㅤワイㅤ, image=ㅤテケiㅤ, anchor="nw", tags="VECTOR_PATH")
                        if not hasattr(self.ᡥᡡᠸᠠᠨ, 'ㅤ_pil_cache'): self.ᡥᡡᠸᠠᠨ.ㅤ_pil_cache = {}
                        self.ᡥᡡᠸᠠᠨ.ㅤ_pil_cache[ㅤウيタㅤ] = ㅤピルاㅤ

                for ㅤチلドㅤ in ㅤノドرㅤ: _ㅤトカシㅤ(ㅤチلドㅤ)

            _ㅤトカシㅤ(ㅤメネジㅤ)
            messagebox.showinfo("만세", "원시 좌표 해석으로 도화지에 불러왔습니다.")
        except Exception as ㅤエラرㅤ:
            messagebox.showerror("실패", f"신비로운 변환 실패:\n{ㅤエラرㅤ}")

    # ══════════════════════════════════════════════════
    # ᡠᠯᡥᡳ ᡳᠴᡳ — Private Helpers / 私有方法
    # ══════════════════════════════════════════════════

    def _ᡤᠰ_ᡥᡡᠸᠠᠨ_ᡩᡝ(self, ᡶᠠᡭ_ᠵᡠᡵᡤᠠᠨ: str) -> bool:
        """
        ᡤᠰ ᡩᡝ ᡥᡡᠸᠠᠨ — Ghostscript 로 .ai/.eps 래스터화 → 캔버스 삽입
        ᡤᠰ ᠠᡤᡡᡵᠠ ᠪᡝ ᡝᡴᠰᡳᡴᡡᡨᡳ ─ Execute GS and paste result
        """
        try:
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as ᡨᡝᠮᡶ:
                ᡨᡝᠮᡶ_ᠵᡠᡵᡤᠠᠨ = ᡨᡝᠮᡶ.name

            ᠴᠣᡴᡡᠨ = self.ᡥᡡᠸᠠᠨ.winfo_width()  or 1400
            ᡩᡝᡵᡤᡳ = self.ᡥᡡᠸᠠᠨ.winfo_height() or 900

            # ── Ghostscript 명령 ──
            ᠺᠣᠮᠠᠨᡩ = [
                _ᡤᠰ_ᠵᡠᡵᡤᡝᠨ,
                "-dBATCH",
                "-dNOPAUSE",
                "-dSAFER",
                "-dNOPROMPT",
                f"-sDEVICE=png16m",
                f"-r{_ᡩᠣᠰᡳ_ᡳᠯᡝᡨᡠᠨ}",
                f"-dDEVICEWIDTHPOINTS={ᠴᠣᡴᡡᠨ}",
                f"-dDEVICEHEIGHTPOINTS={ᡩᡝᡵᡤᡳ}",
                f"-sOutputFile={ᡨᡝᠮᡶ_ᠵᡠᡵᡤᠠᠨ}",
                ᡶᠠᡭ_ᠵᡠᡵᡤᠠᠨ,
            ]

            ᡵᡝᠰᡠᠯᡨ = subprocess.run(
                ᠺᠣᠮᠠᠨᡩ,
                capture_output=True, timeout=30
            )

            if ᡵᡝᠰᡠᠯᡨ.returncode != 0 or not os.path.exists(ᡨᡝᠮᡶ_ᠵᡠᡵᡤᠠᠨ):
                return False

            with open(ᡨᡝᠮᡶ_ᠵᡠᡵᡤᠠᠨ, "rb") as ᡶ:
                ᠫᠨᡤ_ᡩᠠᡨᠠ = ᡶ.read()

            os.unlink(ᡨᡝᠮᡶ_ᠵᡠᡵᡤᠠᠨ)
            return self._ᡳᠮᠠᡤᡝ_ᡩᡝ(ᠫᠨᡤ_ᡩᠠᡨᠠ)

        except Exception:
            return False

    def _ᡴᠠᠨᡳᠪᠠᠰᠠ_ᡤᡝᠮᡠᠯᡝ(self, ᠪᡡᡴᡡ, ᠴᠣᡴᡡᠨ, ᡩᡝᡵᡤᡳ, rl_colors):
        """
        ᡴᠠᠨᡳᠪᠠᠰᠠ ᡩᡝ ᡥᡝᡵᡤᡝᠨ — 캔버스 객체 → reportlab PDF 명령 변환
        ᡠᠯᡥᡳᠶᠠ ᡩᡝ ᡥᡡᠸᠠᠨ ᠪᡝ ᡴᡡᠨᡩᡠᠯᡝᠮᠪᡳ — iterate canvas items
        """
        def _ᠵᠠᠯᡳ(ᠬ: str, fallback=(0, 0, 0)):
            """ᠬ ᠪᡝ ᡥᡝᡵᡤᡝᠨ — color string to (r,g,b) 0-1"""
            if not ᠬ:
                return None
            try:
                ᡵ, ᡤ, ᠪ = self.ᡥᡡᠸᠠᠨ.winfo_rgb(ᠬ)
                return rl_colors.Color(ᡵ/65535, ᡤ/65535, ᠪ/65535)
            except Exception:
                return rl_colors.black

        def _ᠶ(ᡨᡴ_ᠶ): return ᡩᡝᡵᡤᡳ - ᡨᡴ_ᠶ   # ᠶ ᠪᡝ ᠯᠠᡨᡠ — y-flip

        for ᠣᠪᠵ in self.ᡥᡡᠸᠠᠨ.find_all():
            ᡨᠣᡴᠣ = self.ᡥᡡᠸᠠᠨ.type(ᠣᠪᠵ)           # type
            ᠵᠠ   = self.ᡥᡡᠸᠠᠨ.coords(ᠣᠪᠵ)          # coords
            ᡝᡵᡤᡳ = self.ᡥᡡᠸᠠᠨ.itemconfig(ᠣᠪᠵ)      # config

            ᡥᠣᠯᠣ_ᠬ = 设(ᡝᡵᡤᡳ, 'outline')   # outline color
            ᡩᡳᠮᠪᡠ_ᠬ = 设(ᡝᡵᡤᡳ, 'fill')      # fill color
            ᠨᡳᠶᠠᠨᠯᡳᠨ = float(设(ᡝᡵᡤᡳ, 'width') or 1)

            try:
                if ᡨᠣᡴᠣ == "line" and len(ᠵᠠ) >= 4:
                    ᠪᡡᡴᡡ.setStrokeColor(_ᠵᠠᠯᡳ(ᡩᡳᠮᠪᡠ_ᠬ or ᡥᠣᠯᠣ_ᠬ))
                    ᠪᡡᡴᡡ.setLineWidth(ᠨᡳᠶᠠᠨᠯᡳᠨ)
                    ᡶ = ᠪᡡᡴᡡ.beginPath()
                    ᡶ.moveTo(ᠵᠠ[0], _ᠶ(ᠵᠠ[1]))
                    for ᡳ in range(2, len(ᠵᠠ)-1, 2):
                        ᡶ.lineTo(ᠵᠠ[ᡳ], _ᠶ(ᠵᠠ[ᡳ+1]))
                    ᠪᡡᡴᡡ.drawPath(ᡶ, stroke=1, fill=0)

                elif ᡨᠣᡴᠣ == "rectangle" and len(ᠵᠠ) >= 4:
                    x1,y1,x2,y2 = ᠵᠠ[:4]
                    ᠪᡡᡴᡡ.setStrokeColor(_ᠵᠠᠯᡳ(ᡥᠣᠯᠣ_ᠬ))
                    ᠪᡡᡴᡡ.setFillColor(_ᠵᠠᠯᡳ(ᡩᡳᠮᠪᡠ_ᠬ) or rl_colors.transparent)
                    ᠪᡡᡴᡡ.setLineWidth(ᠨᡳᠶᠠᠨᠯᡳᠨ)
                    ᠪᡡᡴᡡ.rect(min(x1,x2), _ᠶ(max(y1,y2)),
                              abs(x2-x1), abs(y2-y1),
                              stroke=1 if ᡥᠣᠯᠣ_ᠬ else 0,
                              fill=1 if ᡩᡳᠮᠪᡠ_ᠬ else 0)

                elif ᡨᠣᡴᠣ == "oval" and len(ᠵᠠ) >= 4:
                    x1,y1,x2,y2 = ᠵᠠ[:4]
                    cx,cy = (x1+x2)/2, (y1+y2)/2
                    rx,ry = abs(x2-x1)/2, abs(y2-y1)/2
                    ᠪᡡᡴᡡ.setStrokeColor(_ᠵᠠᠯᡳ(ᡥᠣᠯᠣ_ᠬ))
                    ᠪᡡᡴᡡ.setFillColor(_ᠵᠠᠯᡳ(ᡩᡳᠮᠪᡠ_ᠬ) or rl_colors.transparent)
                    ᠪᡡᡴᡡ.ellipse(cx-rx, _ᠶ(cy)-ry, cx+rx, _ᠶ(cy)+ry,
                                 stroke=1, fill=1 if ᡩᡳᠮᠪᡠ_ᠬ else 0)

                elif ᡨᠣᡴᠣ == "text" and len(ᠵᠠ) >= 2:
                    ᡩᡝ = 设(ᡝᡵᡤᡳ, 'text')
                    ᡶᠣᠨᡨ_ᡳ = 设(ᡝᡵᡤᡳ, 'font')
                    ᠪᡡᡴᡡ.setFillColor(_ᠵᠠᠯᡳ(ᡩᡳᠮᠪᡠ_ᠬ or "black"))
                    try:
                        ᡴᡳᡴᡝ = int(str(ᡶᠣᠨᡨ_ᡳ).split()[-1])
                    except Exception:
                        ᡴᡳᡴᡝ = 12
                    ᠪᡡᡴᡡ.setFont("Helvetica", max(6, ᡴᡳᡴᡝ))
                    ᠪᡡᡴᡡ.drawCentredString(ᠵᠠ[0], _ᠶ(ᠵᠠ[1]), ᡩᡝ)

            except Exception:
                pass   # ᡠᠯᡥᡳ ᡳ ᡩᡡᠯᡝ — skip failed object

        ᠪᡡᡴᡡ.showPage()

    def _ᡳᠮᠠᡤᡝ_ᡩᡝ(self, ᠫᠨᡤ_ᡩᠠᡨᠠ: bytes) -> bool:
        """
        ᡳᠮᠠᡤᡝ ᡩᡝ ᡥᡡᠸᠠᠨ — PNG 바이트 → PhotoImage → 캔버스 중앙 삽입
        ᡠᠯᡥᡳᠶᠠ ᡩᡝ ᡥᡡᠸᠠᠨ ᡩᡝ ᡤᡡᡵᡝ — attach image to canvas
        """
        try:
            from PIL import Image, ImageTk
            ᡳᠮᡤ = Image.open(io.BytesIO(ᠫᠨᡤ_ᡩᠠᡨᠠ))
            ᠴ = self.ᡥᡡᠸᠠᠨ.winfo_width()  or 1400
            ᡩ = self.ᡥᡡᠸᠠᠨ.winfo_height() or 900
            ᡳᠮᡤ.thumbnail((ᠴ, ᡩ), Image.Resampling.LANCZOS)
            ᡨᡴ_ᡳᠮᡤ = ImageTk.PhotoImage(ᡳᠮᡤ)

            # 캐시 참조 유지 (GC 방지)
            if not hasattr(self.ᡥᡡᠸᠠᠨ, '_ᡳᠮᠠᡤᡝ_ᡴᠠᡧ'):
                self.ᡥᡡᠸᠠᠨ._ᡳᠮᠠᡤᡝ_ᡴᠠᡧ = []
            self.ᡥᡡᠸᠠᠨ._ᡳᠮᠠᡤᡝ_ᡴᠠᡧ.append(ᡨᡴ_ᡳᠮᡤ)

            self.ᡥᡡᠸᠠᠨ.create_image(ᠴ//2, ᡩ//2,
                                    image=ᡨᡴ_ᡳᠮᡤ, anchor="center")
            return True
        except Exception:
            return False


# ══════════════════════════════════════════════════════
# ᠠᡤᡡᡵᠠ ᡤᡳᠰᡠᠨ — Helper / util functions
# ══════════════════════════════════════════════════════
def 设(ᡝᡵᡤᡳ: dict, ᡴᡝ: str, fallback: str = "") -> str:
    """ᡝᡵᡤᡳ ᡩᡝ ᡴᡝ ᡤᠠᠵᡳ — get itemconfig value safely
    ᡝᡵᡤᡳ = config dict, ᡴᡝ = key, fallback = default"""
    try:
        return str(ᡝᡵᡤᡳ.get(ᡴᡝ, ['','','','', fallback])[-1])
    except Exception:
        return fallback
