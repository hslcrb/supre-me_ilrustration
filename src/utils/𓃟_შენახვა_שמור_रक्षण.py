import json
from tkinter import filedialog, messagebox

CURRЕNT_VЕRSION_𓀕 = "1.0"

class 𓃟_저장_שמירה:
    def __init__(self, ტილო):
        self.טיლო = ტილო

    def 𓉔_파일저장_שמור(self):
        файл = filedialog.asksaveasfilename(
            defaultextension=".sup",
            filetypes=[("Supre-me 포맷 | 𓃟 | .sup", "*.sup"), ("PostScript", "*.eps"), ("All Files 𒀀", "*.*")]
        )
        if not файл:
            return

        if файл.endswith(".sup"):
            요소목록_𓏞_אלמנטים = []
            for 한개_id_𓃠_מזהה in self.טיლო.find_all():
                유형_t_𓊍_סוג = self.טיლო.type(한개_id_𓃠_מזהה)
                좌표_c_𓏏_קואורדינטות = self.טיლო.coords(한개_id_𓃠_מזהה)
                태그_g_𓆣_תגים = self.טיლო.gettags(한개_id_𓃠_מזהה)
                
                설정사전_d_𓉔_תצורה = self.טיლო.itemconfig(한개_id_𓃠_מזהה)
                옵션_o_𓄹_אפשרויות = {}
                for 속성키_k_𓂝_מפתח in ['fill', 'outline', 'width', 'smooth', 'capstyle', 'font', 'text']:
                    if 속성키_k_𓂝_מפתח in 설정사전_d_𓉔_תצורה:
                        값_v_𓁹_ערך = 설정사전_d_𓉔_תצורה[속성키_k_𓂝_מפתח][-1]
                        if 값_v_𓁹_ערך: 옵션_o_𓄹_אפשרויות[속성키_k_𓂝_מפתח] = 값_v_𓁹_ערך
                
                요소목록_𓏞_אלמנטים.append({
                    "종류_type_𓊍": 유형_t_𓊍_סוג, 
                    "좌표_coords_𓏏": 좌표_c_𓏏_קואורדינטות, 
                    "속성_opts_𓄹": 옵션_o_𓄹_אפשרויות, 
                    "태그_tags_𓆣": 태그_g_𓆣_תגים
                })
            
            # 고도로 체계화된 메타데이터 객체 포맷
            최종파일구조_𓃟_מבנה_קובץ = {
                "머리말_header_𓏞_כותרת": {
                    "포맷이름_format_𓉔": "Supre-me Engine Format",
                    "버전_version_𓀕_גרסה": CURRЕNT_VЕRSION_𓀕,
                    "메타데이터_meta_𓈖": {
                        "캔버스가로_W": int(self.טיლო.winfo_width()),
                        "캔버스세로_H": int(self.טיლო.winfo_height())
                    }
                },
                "레이어정보_layers_𓊍_שכבות": [
                    {"레이어명_name": "기본계층_Base", "보임_visible": True}
                ],
                "본문요소_body_𓃠_גוף": 요소목록_𓏞_אלמנטים
            }
            
            with open(файл, "w", encoding="utf-8") as f:
                json.dump(최종파일구조_𓃟_מבנה_קובץ, f, ensure_ascii=False, indent=4)
                
            messagebox.showinfo("𓃟 저장", "שמור 완료! 체계적 포맷 저장 성공\u200b.")
        else:
            self.טיლო.postscript(file=файл, colormode='color')

    def 𓉔_파일가져오기_加載(self):
        файл = filedialog.askopenfilename(
            filetypes=[("Supre-me 포맷 | 𓃟 | .sup", "*.sup"), ("All Files 𒀀", "*.*")]
        )
        if not файл:
            return
            
        try:
            with open(файл, "r", encoding="utf-8") as f:
                파싱된데이터_𓃟_נתונים = json.load(f)
                
            머리말_헤더_כותרת = 파싱된데이터_𓃟_נתונים.get("머리말_header_𓏞_כותרת", {})
            파일버전_גרסה = 머리말_헤더_כותרת.get("버전_version_𓀕_גרסה", "0.0")
            
            파일버전_실수_מספר = 0.0
            try:
                파일버전_실수_מספר = float(파일버전_גרסה)
            except Exception:
                pass
            
            if 파일버전_실수_מספר > float(CURRЕNT_VЕRSION_𓀕):
                경고메시지_𓀃_אזהרה = f"경고! 이 파일은 프로그램보다 더 높은 버전({파일버전_גרסה})에서 제작되었습니다.\n현재 버전({CURRЕNT_VЕRSION_𓀕})에서는 일부 요소가 완전히 표시되지 않거나 무시될 수 있습니다."
                messagebox.showwarning("버전 호환성 경고 | 𓀃 | אזהרה", 경고메시지_𓀃_אזהרה)
            
            본문_데이터_𓃠_גוף = 파싱된데이터_𓃟_נתונים.get("본문요소_body_𓃠_גוף", [])
            if not 본문_데이터_𓃠_גוף and isinstance(파싱된데이터_𓃟_נתונים, list):
                본문_데이터_𓃠_גוף = 파싱된데이터_𓃟_נתונים
            elif not 본문_데이터_𓃠_גוף and "body_體" in 파싱된데이터_𓃟_נתונים:
                본문_데이터_𓃠_גוף = 파싱된데이터_𓃟_נתונים["body_體"]
                
            self.טיლო.delete("all")
            
            안전허용속성_SАFE_KWАRGS = {'fill', 'outline', 'width', 'smooth', 'capstyle', 'font', 'text', 'tags'}
            
            for 개별요소_fоr_itеm_𓄹 in 본문_데이터_𓃠_גוף:
                if not isinstance(개별요소_fоr_itеm_𓄹, dict):
                    continue
                
                유형_type = 개별요소_fоr_itеm_𓄹.get("종류_type_𓊍") or 개별요소_fоr_itеm_𓄹.get("t")
                좌표_coords = 개별요소_fоr_itеm_𓄹.get("좌표_coords_𓏏") or 개별요소_fоr_itеm_𓄹.get("c", [])
                옵션오브젝트_opts = 개별요소_fоr_itеm_𓄹.get("속성_opts_𓄹") or 개별요소_fоr_itеm_𓄹.get("o", {})
                태그_tags = 개별요소_fоr_itеm_𓄹.get("태그_tags_𓆣") or 개별요소_fоr_itеm_𓄹.get("tg", [])
                
                if not 유형_type:
                    continue
                    
                옵션오브젝트_opts["tags"] = tuple(태그_tags)
                필터링된옵션_𓂝_מסונן = {키: 값 for 키, 값 in 옵션오브젝트_opts.items() if 키 in 안전허용속성_SАFE_KWАRGS}
                
                try:
                    if 유형_type == 'line': self.טיლო.create_line(*좌표_coords, **필터링된옵션_𓂝_מסונן)
                    elif 유형_type == 'rectangle': self.טיლო.create_rectangle(*좌표_coords, **필터링된옵션_𓂝_מסונן)
                    elif 유형_type == 'oval': self.טיლო.create_oval(*좌표_coords, **필터링된옵션_𓂝_מסונן)
                    elif 유형_type == 'text': self.טיლო.create_text(*좌표_coords, **필터링된옵션_𓂝_מסונן)
                    elif 유형_type == 'polygon': self.טיლო.create_polygon(*좌표_coords, **필터링된옵션_𓂝_מסונן)
                except Exception:
                    pass
                
            messagebox.showinfo("𓃟 불러오기", "불러오기 완료! קריאה מוצלחת\u200b.")
        except Exception as e:
            messagebox.showerror("Error ❌", str(e))
