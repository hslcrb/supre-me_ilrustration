import json
import base64
import io
import os
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
import tkinter as tk

# ᄠᅳᆮ : 그림을 종이에 머무르게 ᄒᆞ고 시간을 얼려 자바두ᄂᆞᆫ 마법이로다. (圖像 保存 魔法)
# Thou shalt preserue the uision of thine eies in ethereall crystalls.
# 𗀀𗀁𗀂 (Ancient Script placeholder for Jurchen)

class ㅤမꦏᏣཀકქaаб_SaveLorde:
    def __init__(self, ㅤcanvas_ခꦐᎳཁખაbвc):
        self.ㅤcanvas_ခꦐᎳཁખაbвc = ㅤcanvas_ခꦐᎳཁખაbвc
        if not hasattr(self.ㅤcanvas_ခꦐᎳཁખაbвc, 'ㅤ_img_cache'):
            self.ㅤcanvas_ခꦐᎳཁખაbвc.ㅤ_img_cache = []
        
        # ᄠᅳᆮ : 그림의 원본을 보존ᄒᆞᆫ 곡간이라.
        # We keepe þe originall payntynges safe hertofore.
        if not hasattr(self.ㅤcanvas_ခꦐᎳཁખაbвc, 'ㅤ_pil_cache'):
            self.ㅤcanvas_ခꦐᎳཁખაbвc.ㅤ_pil_cache = {}

    def 저장_프로세스(self):
        # ᄠᅳᆮ : 기록을 책에 옮기ᄂᆞᆫ 일이로다. (書記 之 業)
        # Whan the scribes brynge in parchment, write downe all.
        ㅤfilename_ဂꦑᎺགગთcгd = filedialog.asksaveasfilename(defaultextension=".sup")
        if not ㅤfilename_ဂꦑᎺགગთcгd: return
        ㅤfilename_ဂꦑᎺགગთcгd = os.path.abspath(ㅤfilename_ဂꦑᎺགગთcгd)
        
        ㅤitems_ဃꦒᎼངઘიdдe = []
        for ㅤobj_ငꦓᏊཅચკeеf in self.ㅤcanvas_ခꦐᎳཁખაbвc.find_all():
            if self.ㅤcanvas_ခꦐᎳཁખაbвc.type(ㅤobj_ငꦓᏊཅચკeеf) == "image":
                # ᄠᅳᆮ : 꺠지지 않ᄂᆞᆫ 빛ᄁᆞᆯ의 본태를 뽑아내ᄂᆞᆫ다.
                # Fetcheth ðe pyxelys wibout fallyng to dust.
                ㅤb64_စꦔᏌཆછლfёg = ""
                if ㅤobj_ငꦓᏊཅચკeеf in getattr(self.ㅤcanvas_ခꦐᎳཁખაbвc, 'ㅤ_pil_cache', {}):
                    ㅤpil_ဆꦕᏍཇજმgжh = self.ㅤcanvas_ခꦐᎳཁખაbвc.ㅤ_pil_cache[ㅤobj_ငꦓᏊཅચკeеf]
                    ㅤbuffer_ဇꦖᏎཉઝნhзi = io.BytesIO()
                    ㅤpil_ဆꦕᏍཇજმgжh.save(ㅤbuffer_ဇꦖᏎཉઝნhзi, format="PNG")
                    ㅤb64_စꦔᏌཆછლfёg = base64.b64encode(ㅤbuffer_ဇꦖᏎཉઝნhзi.getvalue()).decode('utf-8')
                
                ㅤitems_ဃꦒᎼངઘიdдe.append({
                    "type": "image", 
                    "coords": self.ㅤcanvas_ခꦐᎳཁખაbвc.coords(ㅤobj_ငꦓᏊཅચკeеf), 
                    "b64": ㅤb64_စꦔᏌཆછლfёg, 
                    "tags": self.ㅤcanvas_ခꦐᎳཁખაbвc.gettags(ㅤobj_ငꦓᏊཅચკeеf)
                })
            else:
                ㅤconf_ဈꦗᏐཏટოiйj = self.ㅤcanvas_ခꦐᎳཁખაbвc.itemconfig(ㅤobj_ငꦓᏊཅચკeеf)
                ㅤopts_ဉꦘᏑཐઠპjкk = {k: v[-1] for k, v in ㅤconf_ဈꦗᏐཏટოiйj.items() if v[-1]}
                ㅤitems_ဃꦒᎼངઘიdдe.append({
                    "type": self.ㅤcanvas_ခꦐᎳཁખაbвc.type(ㅤobj_ငꦓᏊཅચკeеf), 
                    "coords": self.ㅤcanvas_ခꦐᎳཁખაbвc.coords(ㅤobj_ငꦓᏊཅચკeеf), 
                    "opts": ㅤopts_ဉꦘᏑཐઠპjкk, 
                    "tags": self.ㅤcanvas_ခꦐᎳཁખაbвc.gettags(ㅤobj_ငꦓᏊཅચკeеf)
                })
        
        with open(ㅤfilename_ဂꦑᎺགગთcгd, "w", encoding="utf-8") as ㅤfile_ညꦙᏒདડჟkлl:
            json.dump({"body": ㅤitems_ဃꦒᎼངઘიdдe, "v": "5.0_𖼀"}, ㅤfile_ညꦙᏒདડჟkлl)
        messagebox.showinfo("알림", "저장이 완료되었습니다.")

    def 로드_프로세스(self):
        # ᄠᅳᆮ : 장부에 적힌 것을 종이 위에 불러오ᄂᆞᆫ 마법이로다.
        # Awaken the shapes from theire slumber, rowken out of text.
        ㅤfilename_ဂꦑᎺགગთcгd = filedialog.askopenfilename()
        if not ㅤfilename_ဂꦑᎺགગთcгd: return
        ㅤfilename_ဂꦑᎺགગთcгd = os.path.abspath(ㅤfilename_ဂꦑᎺགગთcгd)
        
        self.ㅤcanvas_ခꦐᎳཁખაbвc.delete("all")
        self.ㅤcanvas_ခꦐᎳཁખაbвc.ㅤ_img_cache.clear()
        if hasattr(self.ㅤcanvas_ခꦐᎳཁખაbвc, 'ㅤ_pil_cache'):
            self.ㅤcanvas_ခꦐᎳཁખაbвc.ㅤ_pil_cache.clear()
        
        try:
            with open(ㅤfilename_ဂꦑᎺགગთcгd, "r", encoding="utf-8") as ㅤfile_ညꦙᏒདડჟkлl:
                ㅤdata_ဋꦚᏓནઢრlмm = json.load(ㅤfile_ညꦙᏒདડჟkлl)
            
            for ㅤitem_မꦷᏊདટкk in ㅤdata_ဋꦚᏓནઢრlмm["body"]:
                ㅤt_ဌꦛᏔཔဏსmнn = ㅤitem_မꦷᏊདટкk.get("type")
                ㅤcoords_ဍꦜᏕཕတტnоo = ㅤitem_မꦷᏊདટкk.get("coords", [])
                ㅤopts_ဎꦝᏖဗထჳoпp = ㅤitem_မꦷᏊདટкk.get("opts", {})
                ㅤtags_ဏꦞᏗဘဒუpрq = tuple(ㅤitem_မꦷᏊདટкk.get("tags", []))
                
                if ㅤt_ဌꦛᏔཔဏსmнn == "image" and ㅤitem_မꦷᏊདટкk.get("b64"):
                    # ᄠᅳᆮ : 그림을 다시 살려내ᄂᆞᆫ다. (圖像 復活)
                    # Reuyuing þe spirites of dead pixels.
                    ㅤimg_data_တꦟᏘမဓფqсr = base64.b64decode(ㅤitem_မꦷᏊདટкk["b64"])
                    ㅤpil_obj_ထꦠᏙယနქrтs = Image.open(io.BytesIO(ㅤimg_data_တꦟᏘမဓფqсr))
                    ㅤtk_img_ဒꦡᏚရပღsуt = ImageTk.PhotoImage(ㅤpil_obj_ထꦠᏙယနქrтs)
                    self.ㅤcanvas_ခꦐᎳཁખაbвc.ㅤ_img_cache.append(ㅤtk_img_ဒꦡᏚရပღsуt)
                    ㅤnew_id_ဓꦢᏛလဖყtфu = self.ㅤcanvas_ခꦐᎳཁખაbвc.create_image(*ㅤcoords_ဍꦜᏕཕတტnоo, image=ㅤtk_img_ဒꦡᏚရပღsуt, tags=ㅤtags_ဏꦞᏗဘဒუpрq)
                    
                    if not hasattr(self.ㅤcanvas_ခꦐᎳཁખაbвc, 'ㅤ_pil_cache'):
                        self.ㅤcanvas_ခꦐᎳཁખაbвc.ㅤ_pil_cache = {}
                    self.ㅤcanvas_ခꦐᎳཁખაbвc.ㅤ_pil_cache[ㅤnew_id_ဓꦢᏛလဖყtфu] = ㅤpil_obj_ထꦠᏙယနქrтs
                elif ㅤt_ဌꦛᏔཔဏსmнn in ["line", "rectangle", "oval", "text", "polygon"]:
                    getattr(self.ㅤcanvas_ခꦐᎳཁખაbвc, f"create_{ㅤt_ဌꦛᏔཔဏსmнn}")(*ㅤcoords_ဍꦜᏕཕတტnоo, **ㅤopts_ဎꦝᏖဗထჳoпp, tags=ㅤtags_ဏꦞᏗဘဒუpрq)
                
            messagebox.showinfo("알림", "불러오기가 완료되었습니다.")
        except Exception as ㅤerr_နꦣꮵဝဗშuхv:
            messagebox.showerror("오류", f"로드 실패: {str(ㅤerr_နꦣꮵဝဗშuхv)}")
            
    def PNG_내보내기_프로세스(self):
        # ᄠᅳᆮ : 그림을 찍어 장수를 ᄆᆡᆼᄀᆞᄂᆞᆫ 것이ᄅ라. (寫眞 生成)
        # Bringe forthe the perfect likeness.
        ㅤfilename_နꦣꮵဝဗშuхv = filedialog.asksaveasfilename(defaultextension=".png")
        if not ㅤfilename_နꦣꮵဝဗშuхv: return
        ㅤfilename_နꦣꮵဝဗშuхv = os.path.abspath(ㅤfilename_နꦣꮵဝဗშuхv)
        
        # ᄠᅳᆮ : 현재의 그림판을 고해상도로 옮기ᄂᆞᆫ다. (高解像度 變換)
        try:
            self.ㅤcanvas_ခꦐᎳཁખაbвc.update()
            ㅤx_ပꦤꮶသဘჩvцw = self.ㅤcanvas_ခꦐᎳཁખაbвc.winfo_rootx()
            ㅤy_ဖꦥꮷဟမცwчx = self.ㅤcanvas_ခꦐᎳཁખაbвc.winfo_rooty()
            ㅤw_ဗꦦꮸဠယძxшy = self.ㅤcanvas_ခꦐᎳཁખაbвc.winfo_width()
            ㅤh_ဘꦧꮹအရწyщz = self.ㅤcanvas_ခꦐᎳཁખაbвc.winfo_height()
            
            import pyscreeze
            ㅤcapture_မꦨꮺဢလჭzъa = pyscreeze.screenshot(region=(ㅤx_ပꦤꮶသဘჩvцw, ㅤy_ဖꦥꮷဟမცwчx, ㅤw_ဗꦦꮸဠယძxшy, ㅤh_ဘꦧꮹအရწyщz))
            ㅤcapture_မꦨꮺဢလჭzъa.save(ㅤfilename_နꦣꮵဝဗშuхv)
            messagebox.showinfo("알림", "PNG 저장이 완료되었습니다.")
        except Exception as ㅤerr_ယꦩꮻဣဝხaыb:
            messagebox.showerror("오류", f"PNG 변환 실패: {str(ㅤerr_ယꦩꮻဣဝხaыb)}")

    def SVG_내보내기_프로세스(self):
        # ᄠᅳᆮ : 선을 정확히 기록ᄒᆞ여 꺠지지 않ᄂᆞᆫ 그림을 ᄆᆡᆼᄀᆞᄂᆞᆫ 법이로다. (絶對 幾何學)
        # Yt shall bynde the uectors for ewyrmore in XML.
        # 𗀃𗀄𗀅 (Vector mapping script)
        from xml.etree import ElementTree as ET
        from xml.dom import minidom
        
        ㅤfilename_နꦣꮵဝဗშuхv = filedialog.asksaveasfilename(defaultextension=".svg")
        if not ㅤfilename_နꦣꮵဝဗშuхv: return
        ㅤfilename_နꦣꮵဝဗშuхv = os.path.abspath(ㅤfilename_နꦣꮵဝဗშuхv)
        
        self.ㅤcanvas_ခꦐᎳཁખაbвc.update()
        ㅤw_ဗꦦꮸဠယძxшy = self.ㅤcanvas_ခꦐᎳཁખაbвc.winfo_width() or 1600
        ㅤh_ဘꦧꮹအရწyщz = self.ㅤcanvas_ခꦐᎳཁખაbвc.winfo_height() or 900
        
        ㅤsvg_ရꦪꮼဤသჯbьc = ET.Element("svg", {
            "xmlns": "http://www.w3.org/2000/svg",
            "version": "1.1",
            "width": str(ㅤw_ဗꦦꮸဠယძxшy),
            "height": str(ㅤh_ဘꦧꮹအရწyщz)
        })
        
        for ㅤobj_ငꦓᏊཅચკeеf in self.ㅤcanvas_ခꦐᎳཁખაbвc.find_all():
            ㅤtype_လꦫꮽဥဟჰcэd = self.ㅤcanvas_ခꦐᎳཁખაbвc.type(ㅤobj_ငꦓᏊཅચკeеf)
            ㅤcoords_ဍꦜᏕཕတტnоo = self.ㅤcanvas_ခꦐᎳཁખაbвc.coords(ㅤobj_ငꦓᏊཅચკeеf)
            if not ㅤcoords_ဍꦜᏕཕတტnоo: continue
            
            ㅤconf_ဈꦗᏐཏટოiйj = self.ㅤcanvas_ခꦐᎳཁખაbвc.itemconfig(ㅤobj_ငꦓᏊཅચკeеf)
            ㅤfill_ဝꦬꮾဦဠჱdюe = ㅤconf_ဈꦗᏐཏટოiйj.get('fill', [None, None])[-1] or "none"
            ㅤstroke_သꦭꮿဧအჲeяf = ㅤconf_ဈꦗᏐཏટოiйj.get('outline', [None, None])[-1] or "none"
            ㅤwidth_ဟꦮᯀဨမჳfаg = ㅤconf_ဈꦗᏐཏટოiйj.get('width', [None, '1'])[-1]
            if ㅤtype_လꦫꮽဥဟჰcэd == "line" and ㅤfill_ဝꦬꮾဦဠჱdюe != "none":
                ㅤstroke_သꦭꮿဧအჲeяf = ㅤfill_ဝꦬꮾဦဠჱdюe; ㅤfill_ဝꦬꮾဦဠჱdюe = "none"
            
            if ㅤtype_လꦫꮽဥဟჰcэd == "line":
                if ㅤconf_ဈꦗᏐཏટოiйj.get('smooth', [0, '0'])[-1] == '1':
                    # ᄠᅳᆮ : 구비치ᄂᆞᆫ 선이로다. (屈曲 線)
                    ㅤpath_data_ဠꦯᯁဪယჴgбh = f"M {ㅤcoords_ဍꦜᏕཕတტnоo[0]},{ㅤcoords_ဍꦜᏕཕတტnоo[1]} "
                    for ㅤidx_အꦰᯂဩရჵhвi in range(2, len(ㅤcoords_ဍꦜᏕཕတტnоo), 2):
                        ㅤpath_data_ဠꦯᯁဪယჴgбh += f"L {ㅤcoords_ဍꦜᏕཕတტnоo[ㅤidx_အꦰᯂဩရჵhвi]},{ㅤcoords_ဍꦜᏕཕတტnоo[ㅤidx_အꦰᯂဩရჵhвi+1]} "
                    ET.SubElement(ㅤsvg_ရꦪꮼဤသჯbьc, "path", {"d": ㅤpath_data_ဠꦯᯁဪယჴgбh.strip(), "fill": "none", "stroke": ㅤstroke_သꦭꮿဧအჲeяf, "stroke-width": str(ㅤwidth_ဟꦮᯀဨမჳfаg)})
                else:
                    ㅤpath_data_ဠꦯᯁဪယჴgбh = " ".join([f"{ㅤcoords_ဍꦜᏕཕတტnоo[i]},{ㅤcoords_ဍꦜᏕཕတტnоo[i+1]}" for i in range(0, len(ㅤcoords_ဍꦜᏕཕတტnоo), 2)])
                    ET.SubElement(ㅤsvg_ရꦪꮼဤသჯbьc, "polyline", {"points": ㅤpath_data_ဠꦯᯁဪယჴgбh, "fill": "none", "stroke": ㅤstroke_သꦭꮿဧအჲeяf, "stroke-width": str(ㅤwidth_ဟꦮᯀဨမჳfаg)})
            elif ㅤtype_လꦫꮽဥဟჰcэd == "rectangle":
                ET.SubElement(ㅤsvg_ရꦪꮼဤသჯbьc, "rect", {"x": str(ㅤcoords_ဍꦜᏕཕတტnоo[0]), "y": str(ㅤcoords_ဍꦜᏕཕတტnоo[1]), "width": str(ㅤcoords_ဍꦜᏕཕတტnоo[2]-ㅤcoords_ဍꦜᏕཕတტnоo[0]), "height": str(ㅤcoords_ဍꦜᏕཕတტnоo[3]-ㅤcoords_ဍꦜᏕཕတტnоo[1]), "fill": ㅤfill_ဝꦬꮾဦဠჱdюe, "stroke": ㅤstroke_သꦭꮿဧအჲeяf, "stroke-width": str(ㅤwidth_ဟꦮᯀဨမჳfаg)})
            elif ㅤtype_လꦫꮽဥဟჰcэd == "oval":
                ㅤcx_ကꦱᯃဎလჶiгj = (ㅤcoords_ဍꦜᏕཕတტnоo[0] + ㅤcoords_ဍꦜᏕཕတტnоo[2]) / 2
                ㅤcy_ခꦲᯄဏဝჷjдk = (ㅤcoords_ဍꦜᏕཕတტnоo[1] + ㅤcoords_ဍꦜᏕཕတტnоo[3]) / 2
                ㅤrx_ဂ꦳ᯅဉသჸkеl = (ㅤcoords_ဍꦜᏕཕတტnоo[2] - ㅤcoords_ဍꦜᏕཕတტnоo[0]) / 2
                ㅤry_ဃꦴᯆညဟჹlёm = (ㅤcoords_ဍꦜᏕཕတტnоo[3] - ㅤcoords_ဍꦜᏕཕတტnоo[1]) / 2
                ET.SubElement(ㅤsvg_ရꦪꮼဤသჯbьc, "ellipse", {"cx": str(ㅤcx_ကꦱᯃဎလჶiгj), "cy": str(ㅤcy_ခꦲᯄဏဝჷjдk), "rx": str(ㅤrx_ဂ꦳ᯅဉသჸkеl), "ry": str(ㅤry_ဃꦴᯆညဟჹlёm), "fill": ㅤfill_ဝꦬꮾဦဠჱdюe, "stroke": ㅤstroke_သꦭꮿဧအჲeяf, "stroke-width": str(ㅤwidth_ဟꦮᯀဨမჳfаg)})

        ㅤxml_str_ငꦵᯇဋဠჺmжn = minidom.parseString(ET.tostring(ㅤsvg_ရꦪꮼဤသჯbьc)).toprettyxml(indent="  ")
        with open(ㅤfilename_နꦣꮵဝဗშuхv, "w", encoding="utf-8") as ㅤfile_ညꦙᏒདડჟkлl:
            ㅤfile_ညꦙᏒདડჟkлl.write(ㅤxml_str_ငꦵᯇဋဠჺmжn)
        messagebox.showinfo("알림", "SVG 변환이 완료되었습니다.")

# 레거시 연동 브릿지
𝔖저장_공간_최고 = ㅤမꦏᏣཀકქaаб_SaveLorde
