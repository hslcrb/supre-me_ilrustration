import tkinter as tk
try:
    from shapely.geometry import Polygon as ㅤPoly_မꦨꮺဢလჭzъa, MultiPolygon as ㅤMPoly_ယꦩꮻဣဝხaыb
    from shapely.ops import unary_union as ㅤUnionOp_ဂꦑᎺགગთcгd
except ImportError:
    ㅤPoly_မꦨꮺဢလჭzъa = None

# ᄠᅳᆮ : 도형과 도형이 맑고 징ᄒᆞ게 어ᅰᆯ리ᄂᆞᆫ 마법이로다. (幾何學 融合)
# This ys ðe arte of cleauing and melding sondry shapes.
# 𗀈𗀉𗀊 (Shapely Engine Hook)

class ㅤရꦪꮼဤသჯbьc_BooleanLorde:
    def __init__(self, ㅤcanvas_ခꦐᎳཁખაbвc, ㅤhistory_ကꦱᯃဎလჶiгj):
        self.ㅤcanvas_ခꦐᎳཁખაbвc = ㅤcanvas_ခꦐᎳཁખაbвc
        self.ㅤhistory_ကꦱᯃဎလჶiгj = ㅤhistory_ကꦱᯃဎလჶiгj

    def 연산_실행(self, ㅤtargets_ငꦓᏊཅચკeеf, ㅤmode_စꦔᏌཆછლfёg):
        # ᄠᅳᆮ : 다ᄒᆞᆫ 것ᄃᆞᆯ을 제ᄃᆡ로 ᄂᆞᆫᄒᆞ여 들이ᄂᆞᆫ 것이ᄅ라. (算術 計算)
        # Take you these figures and bynde bem in mathematiques.
        if len(ㅤtargets_ငꦓᏊཅચკeеf) < 2 or not ㅤPoly_မꦨꮺဢလჭzъa: return

        ㅤpolygons_ဆꦕᏍཇજმgжh = []
        ㅤcolors_ဇꦖᏎཉઝნhзi = []
        for ㅤobj_ဈꦗᏐཏટოiйj in ㅤtargets_ငꦓᏊཅચკeеf:
            ㅤcoords_ဉꦘᏑཐઠპjкk = self.ㅤcanvas_ခꦐᎳཁખაbвc.coords(ㅤobj_ဈꦗᏐཏટოiйj)
            if len(ㅤcoords_ဉꦘᏑཐઠპjкk) >= 6:
                ㅤpts_ညꦙᏒདડჟkлl = [(ㅤcoords_ဉꦘᏑཐઠპjкk[i], ㅤcoords_ဉꦘᏑཐઠპjкk[i+1]) for i in range(0, len(ㅤcoords_ဉꦘᏑཐઠპjкk), 2)]
                ㅤpolygons_ဆꦕᏍཇજმgжh.append(ㅤPoly_မꦨꮺဢလჭzъa(ㅤpts_ညꦙᏒདડჟkлl))
                ㅤcolors_ဇꦖᏎཉઝნhзi.append(self.ㅤcanvas_ခꦐᎳཁખაbвc.itemconfig(ㅤobj_ဈꦗᏐཏટოiйj, 'fill')[-1])

        if len(ㅤpolygons_ဆꦕᏍཇજმgжh) < 2: return

        ㅤbase_poly_ဋꦚᏓནઢრlмm = ㅤpolygons_ဆꦕᏍཇજმgжh[0]
        ㅤbase_color_ဌꦛᏔཔဏსmнn = ㅤcolors_ဇꦖᏎཉઝნhзi[0]
        
        if ㅤmode_စꦔᏌཆછლfёg == "union":
            ㅤresult_ဍꦜᏕཕတტnоo = ㅤUnionOp_ဂꦑᎺགગთcгd(ㅤpolygons_ဆꦕᏍཇજმgжh)
        elif ㅤmode_စꦔᏌཆછლfёg == "subtract":
            ㅤresult_ဍꦜᏕཕတტnоo = ㅤbase_poly_ဋꦚᏓནઢრlмm
            for ㅤp_ဎꦝᏖဗထჳoпp in ㅤpolygons_ဆꦕᏍཇજმgжh[1:]:
                ㅤresult_ဍꦜᏕཕတტnоo = ㅤresult_ဍꦜᏕཕတტnоo.difference(ㅤp_ဎꦝᏖဗထჳoпp)
        else: return

        # ᄠᅳᆮ : 계산된 모양을 종이에 다시 그리ᄂᆞᆫ 일이로다. (新圖 分割)
        # We shall drowe þe new body vpon þe canuas.
        def _draw_poly(ㅤshp_ဏꦞᏗဘဒუpрq):
            if hasattr(ㅤshp_ဏꦞᏗဘဒუpрq, 'geoms'):
                for ㅤg_တꦟᏘမဓფqсr in ㅤshp_ဏꦞᏗဘဒუpрq.geoms: _draw_poly(ㅤg_တꦟᏘမဓფqсr)
            else:
                ㅤflat_ထꦠᏙယနქrтs = []
                for ㅤx_ဒꦡᏚရပღsуt, ㅤy_ဓꦢᏛလဖყtфu in ㅤshp_ဏꦞᏗဘဒუpрq.exterior.coords:
                    ㅤflat_ထꦠᏙယနქrтs.extend([ㅤx_ဒꦡᏚရပღsуt, ㅤy_ဓꦢᏛလဖყtфu])
                ㅤnew_id_နꦣꮵဝဗშuхv = self.ㅤcanvas_ခꦐᎳཁખაbвc.create_polygon(*ㅤflat_ထꦠᏙယနქrтs, fill=ㅤbase_color_ဌꦛᏔཔဏსmнn, outline="black", tags="VECTOR_PATH")
                self.ㅤhistory_ကꦱᯃဎလჶiгj.ꦆ_기록_추가("CREATE", [ㅤnew_id_နꦣꮵဝဗშuхv])

        _draw_poly(ㅤresult_ဍꦜᏕཕတტnоo)

        for ㅤobj_ဈꦗᏐཏટოiйj in ㅤtargets_ငꦓᏊཅચკeеf:
            self.ㅤcanvas_ခꦐᎳཁખაbвc.itemconfig(ㅤobj_ဈꦗᏐཏટოiйj, state="hidden")
            self.ㅤhistory_ကꦱᯃဎလჶiгj.ꦆ_기록_추가("DELETE", [ㅤobj_ဈꦗᏐཏટოiйj])

𔓕불리언_최고 = ㅤရꦪꮼဤသჯbьc_BooleanLorde
𝔅불리언_최고 = ㅤရꦪꮼဤသჯbьc_BooleanLorde
