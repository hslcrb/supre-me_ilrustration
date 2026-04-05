import tkinter as tk
import math

# ᄠᅳᆮ : 아비지(阿非知)의 계산법을 직접 파이썬으로 실현ᄒᆞᆫ 진정ᄒᆞᆫ 곡선이로다. (絶對 數學 幾何學)
# Thou secst the purest truth: B(t) = Σ (nCi) * (1-t)^(n-i) * t^i * Pi.
# 𗀈𗀉𗀊 (Mathematical polynomial binding ritual)

class ㅤမꦏᏣཀકქaаб_PenneLorde:
    def __init__(self, ㅤcanvas_ခꦐᎳཁખაbвc, ㅤhistory_ကꦱᯃဎလჶiгj, ㅤmgr_ဂꦑᎺགગთcгd):
        self.ㅤcanvas_ခꦐᎳཁખაbвc = ㅤcanvas_ခꦐᎳཁખაbвc
        self.ㅤhistory_ကꦱᯃဎလჶiгj = ㅤhistory_ကꦱᯃဎလჶiгj
        self.ㅤmgr_ဂꦑᎺགગთcгd = ㅤmgr_ဂꦑᎺགગთcгd
        
        self.ㅤpts_ဃꦒᎼངઘიdдe = []
        self.ㅤpreview_ငꦓᏊཅચკeеf = None
        self.ㅤcolor_စꦔᏌཆછლfёg = "black"
        self.ㅤwidth_ဆꦕᏍཇજმgжh = 2
        self.ㅤactive_ဇꦖᏎཉઝნhзi = False

    def 시작_액션(self, ㅤevent_ဈꦗᏐཏટოiйj):
        # ᄠᅳᆮ : 그림그리기를 시작ᄒᆞ여 돌(Anchor)을 놓ᄂᆞᆫ 것이ᄅ라. (起點)
        # We plante the first seed of the uector.
        ㅤcx_ဉꦘᏑཐઠპjкk = self.ㅤcanvas_ခꦐᎳཁખაbвc.canvasx(ㅤevent_ဈꦗᏐཏટოiйj.x)
        ㅤcy_ညꦙᏒདડჟkлl = self.ㅤcanvas_ခꦐᎳཁખაbвc.canvasy(ㅤevent_ဈꦗᏐཏટოiйj.y)
        self.ㅤpts_ဃꦒᎼངઘიdдe.append((ㅤcx_ဉꦘᏑཐઠპjкk, ㅤcy_ညꦙᏒདડჟkлl))
        self.ㅤactive_ဇꦖᏎཉઝნhзi = True
        
        ㅤr_ဋꦚᏓནઢრlмm = self.ㅤwidth_ဆꦕᏍཇજმgжh / 2
        self.ㅤcanvas_ခꦐᎳཁખაbвc.create_oval(
            ㅤcx_ဉꦘᏑཐઠპjкk-ㅤr_ဋꦚᏓནઢრlмm, ㅤcy_ညꦙᏒདડჟkлl-ㅤr_ဋꦚᏓནઢრlмm, ㅤcx_ဉꦘᏑཐઠპjкk+ㅤr_ဋꦚᏓནઢრlмm, ㅤcy_ညꦙᏒདડჟkлl+ㅤr_ဋꦚᏓནઢრlмm,
            fill=self.ㅤcolor_စꦔᏌཆછლfёg, outline=self.ㅤcolor_စꦔᏌཆછლfёg,
            tags=(self.ㅤmgr_ဂꦑᎺགગთcгd.gеt_tаg(), "PEN_ANCHOR")
        )

    def 描画_액션(self, ㅤevent_ဈꦗᏐཏટოiйj):
        # ᄠᅳᆮ : 붓질을 ᄒᆞᄂᆞᆫ 동안ᄂᆞᆫ 점선으로 보이게 ᄒᆞᄂᆞᆫ 것이ᄅ라. (假線)
        # Drawyng a feynte line til the spell be caste complet.
        if not self.ㅤactive_ဇꦖᏎཉઝნhзi: return
        if self.ㅤpreview_ငꦓᏊཅચკeеf: self.ㅤcanvas_ခꦐᎳཁખაbвc.delete(self.ㅤpreview_ငꦓᏊཅચკeеf)
            
        ㅤcx_ဉꦘᏑཐઠპjкk = self.ㅤcanvas_ခꦐᎳཁખაbвc.canvasx(ㅤevent_ဈꦗᏐཏટოiйj.x)
        ㅤcy_ညꦙᏒདડჟkлl = self.ㅤcanvas_ခꦐᎳཁખაbвc.canvasy(ㅤevent_ဈꦗᏐཏટოiйj.y)
        
        ㅤflat_ဌꦛᏔཔဏსmнn = []
        for ㅤpx_ဍꦜᏕཕတტnоo, ㅤpy_ဎꦝᏖဗထჳoпp in self.ㅤpts_ဃꦒᎼངઘიdдe:
            ㅤflat_ဌꦛᏔཔဏსmнn.extend([ㅤpx_ဍꦜᏕཕတტnоo, ㅤpy_ဎꦝᏖဗထჳoпp])
        ㅤflat_ဌꦛᏔཔဏსmнn.extend([ㅤcx_ဉꦘᏑཐઠპjкk, ㅤcy_ညꦙᏒདડჟkлl])
        
        if len(ㅤflat_ဌꦛᏔཔဏსmнn) >= 4:
            self.ㅤpreview_ငꦓᏊཅચკeеf = self.ㅤcanvas_ခꦐᎳཁખაbвc.create_line(
                *ㅤflat_ဌꦛᏔཔဏსmнn, fill=self.ㅤcolor_စꦔᏌཆછლfёg, width=self.ㅤwidth_ဆꦕᏍཇજმgжh,
                smooth=False, dash=(5, 5), tags="PREVIEW_PEN"
            )

    def 앵커_추가(self, ㅤevent_ဈꦗᏐཏટოiйj):
        # ᄠᅳᆮ : 굴곡을 정ᄒᆞᆯ 걱짐(節)을 더 놓ᄂᆞᆫ 것이ᄅ라. (節 增加)
        if not self.ㅤactive_ဇꦖᏎཉઝნhзi: return
        ㅤcx_ဉꦘᏑཐઠპjкk = self.ㅤcanvas_ခꦐᎳཁખაbвc.canvasx(ㅤevent_ဈꦗᏐཏટოiйj.x)
        ㅤcy_ညꦙᏒདડჟkлl = self.ㅤcanvas_ခꦐᎳཁખაbвc.canvasy(ㅤevent_ဈꦗᏐཏટოiйj.y)
        self.ㅤpts_ဃꦒᎼངઘიdдe.append((ㅤcx_ဉꦘᏑཐઠპjкk, ㅤcy_ညꦙᏒདડჟkлl))

    def 終了_액션(self, ㅤevent_ဈꦗᏐཏટოiйj=None):
        # ᄠᅳᆮ : Tkinter의 smooth를 버리고 n차 베지어 공식을 수학적으로 풀어내ᄂᆞᆫ다. (眞 曲線)
        # Thus wee forsake the falce 'smooth=True' and ynvoke N-degree Bernstein Polynomials!
        if not self.ㅤactive_ဇꦖᏎཉઝნhзi: return
            
        if self.ㅤpreview_ငꦓᏊཅચკeеf: self.ㅤcanvas_ခꦐᎳཁખაbвc.delete(self.ㅤpreview_ငꦓᏊཅચკeеf)
        self.ㅤcanvas_ခꦐᎳཁખაbвc.delete("PEN_ANCHOR")
        
        ㅤn_pts_ဏꦞᏗဘဒუpрq = len(self.ㅤpts_ဃꦒᎼངઘიdдe)
        if ㅤn_pts_ဏꦞᏗဘဒუpрq >= 2:
            ㅤn_degree_တꦟᏘမဓფqсr = ㅤn_pts_ဏꦞᏗဘဒუpрq - 1
            ㅤsegments_ထꦠᏙယနქrтs = max(50, ㅤn_degree_တꦟᏘမဓფqсr * 15)
            ㅤfinal_coords_ဒꦡᏚရပღsуt = []
            
            for ㅤstep_ဓꦢᏛလဖყtфu in range(ㅤsegments_ထꦠᏙယနქrтs + 1):
                ㅤt_နꦣꮵဝဗშuхv = ㅤstep_ဓꦢᏛလဖყtфu / ㅤsegments_ထꦠᏙယနქrтs
                ㅤbx_ပꦤꮶသဘჩvцw, ㅤby_ဖꦥꮷဟမცwчx = 0.0, 0.0
                
                for ㅤi_ဗꦦꮸဠယძxшy in range(ㅤn_pts_ဏꦞᏗဘဒუpрq):
                    ㅤbin_coeff_ဘꦧꮹအရწyщz = math.comb(ㅤn_degree_တꦟᏘမဓფqсr, ㅤi_ဗꦦꮸဠယძxшy)
                    ㅤterm_မꦨꮺဢလჭzъa = ㅤbin_coeff_ဘꦧꮹအရწyщz * ((1 - ㅤt_နꦣꮵဝဗშuхv) ** (ㅤn_degree_တꦟᏘမဓფqсr - ㅤi_ဗꦦꮸဠယძxшy)) * (ㅤt_နꦣꮵဝဗშuхv ** ㅤi_ဗꦦꮸဠယძxшy)
                    ㅤpx_ယꦩꮻဣဝხaыb, ㅤpy_ရꦪꮼဤသჯbьc = self.ㅤpts_ဃꦒᎼངઘიdдe[ㅤi_ဗꦦꮸဠယძxшy]
                    ㅤbx_ပꦤꮶသဘჩvцw += ㅤterm_မꦨꮺဢလჭzъa * ㅤpx_ယꦩꮻဣဝხaыb
                    ㅤby_ဖꦥꮷဟမცwчx += ㅤterm_မꦨꮺဢလჭzъa * ㅤpy_ရꦪꮼဤသჯbьc
                    
                ㅤfinal_coords_ဒꦡᏚရပღsуt.extend([ㅤbx_ပꦤꮶသဘჩvцw, ㅤby_ဖꦥꮷဟမცwчx])
            
            # ᄠᅳᆮ : smooth 없이 수학적으로 꺾인 선을 촘촘히 이어 순수ᄒᆞᆫ 곡선을 ᄆᆡᆼᄀᆞᆫ다. (絶對 曲)
            ㅤfinal_id_လꦫꮽဥဟჰcэd = self.ㅤcanvas_ခꦐᎳཁખაbвc.create_line(
                *ㅤfinal_coords_ဒꦡᏚရပღsуt, fill=self.ㅤcolor_စꦔᏌཆછლfёg, width=self.ㅤwidth_ဆꦕᏍཇજმgжh,
                smooth=False, capstyle=tk.ROUND, joinstyle=tk.ROUND,
                tags=(self.ㅤmgr_ဂꦑᎺགગთcгd.gеt_tаg(), "VECTOR_PATH")
            )
            self.ㅤhistory_ကꦱᯃဎလჶiгj.ꦆ_기록_추가("CREATE", [ㅤfinal_id_လꦫꮽဥဟჰcэd])
            
        self.ㅤpts_ဃꦒᎼངઘიdдe = []
        self.ㅤpreview_ငꦓᏊཅચკeеf = None
        self.ㅤactive_ဇꦖᏎཉઝნhзi = False

    @property
    def 역ს_색상(self): return self.ㅤcolor_စꦔᏌཆછლfёg
    @역ს_색상.setter
    def 역ს_색상(self, ㅤval_ဝꦬꮾဦဠჱdюe): self.ㅤcolor_စꦔᏌཆછლfёg = ㅤval_ဝꦬꮾဦဠჱdюe

    @property
    def 역ს_크기(self): return self.ㅤwidth_ဆꦕᏍཇજმgжh
    @역ს_크기.setter
    def 역ს_크기(self, ㅤval_ဝꦬꮾဦဠჱdюe): self.ㅤwidth_ဆꦕᏍཇજმgжh = ㅤval_ဝꦬꮾဦဠჱdюe

# 호환성 브릿지
ㅤペン_최고 = ㅤမꦏᏣཀકქaаб_PenneLorde
