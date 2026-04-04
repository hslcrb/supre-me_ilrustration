# 𐎁 정렬 및 분포 엔진 (Alignment & Distribution)
# 𝔄 𝔅 ℭ (Fraktur) / क ख (Hindi) / א ב (Hebrew) / ሀ ለ (Ge'ez) / ᆇ (쌍아래아) / 〮 (방점)

class 𝔅정렬_엔진〮:
    def __init__(self, ሐ_cаnvаs, ዮ_hіstоry):
        self.ሐ = ሐ_cаnvаs
        self.역사 = ዮ_hіstоry

    def 정렬_실행(self, о_목록, 모드):
        """
        모드: 'left', 'right', 'hcenter', 'top', 'bottom', 'vcenter', 'dist_h', 'dist_v'
        """
        if not о_목록 or len(о_목록) < 2:
            return

        # 전체 바운딩 박스 계산
        א_min_x = float('inf')
        ב_min_y = float('inf')
        א_max_x = -float('inf')
        ב_max_y = -float('inf')
        
        क_boxes = {}
        
        for obj in о_목록:
            b = self.ሐ.bbox(obj)
            if b:
                क_boxes[obj] = b
                א_min_x = min(א_min_x, b[0])
                ב_min_y = min(ב_min_y, b[1])
                א_max_x = max(א_max_x, b[2])
                ב_max_y = max(ב_max_y, b[3])

        if not क_boxes: return
        
        ሀ_c_x = (א_min_x + א_max_x) / 2
        ለ_c_y = (ב_min_y + ב_max_y) / 2

        for obj, b in क_boxes.items():
            cx = (b[0] + b[2]) / 2
            cy = (b[1] + b[3]) / 2
            w = b[2] - b[0]
            h = b[3] - b[1]
            
            dx, dy = 0, 0
            
            if 모드 == 'left':     dx = א_min_x - b[0]
            elif 모드 == 'right':    dx = א_max_x - b[2]
            elif 모드 == 'hcenter':  dx = ሀ_c_x - cx
            elif 모드 == 'top':      dy = ב_min_y - b[1]
            elif 모드 == 'bottom':   dy = ב_max_y - b[3]
            elif 모드 == 'vcenter':  dy = ለ_c_y - cy
            
            if dx != 0 or dy != 0:
                self.ሐ.move(obj, dx, dy)
                
        # 분포 (Distribution) 로직 
        if 모드 == 'dist_h' and len(क_boxes) > 2:
            sorted_objs = sorted(क_boxes.keys(), key=lambda o: क_boxes[o][0])
            total_w = א_max_x - א_min_x
            sum_w = sum(क_boxes[o][2] - क_boxes[o][0] for o in sorted_objs)
            gap = (total_w - sum_w) / (len(sorted_objs) - 1) if len(sorted_objs) > 1 else 0
            
            curr_x = א_min_x
            for obj in sorted_objs:
                dx = curr_x - क_boxes[obj][0]
                self.ሐ.move(obj, dx, 0)
                curr_x += (क_boxes[obj][2] - क_boxes[obj][0]) + gap
                
        elif 모드 == 'dist_v' and len(क_boxes) > 2:
            sorted_objs = sorted(क_boxes.keys(), key=lambda o: क_boxes[o][1])
            total_h = ב_max_y - ב_min_y
            sum_h = sum(क_boxes[o][3] - क_boxes[o][1] for o in sorted_objs)
            gap = (total_h - sum_h) / (len(sorted_objs) - 1) if len(sorted_objs) > 1 else 0
            
            curr_y = ב_min_y
            for obj in sorted_objs:
                dy = curr_y - क_boxes[obj][1]
                self.ሐ.move(obj, 0, dy)
                curr_y += (क_boxes[obj][3] - क_boxes[obj][1]) + gap

        self.역사.추가_기록(о_목록)
