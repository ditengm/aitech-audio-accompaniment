import sys

sys.path.append("./")
sys.path.append("/app/apex/VinVL/Oscar")
sys.path.append(
    "/app/vinvl-visualbackbone/scene_graph_benchmark"
)
import cv2

from utils.captioner import SceneDescripter

if __name__ == "__main__":
    kpt = "/app/apex/VinVL/Oscar/vinvl-base-image-captioning"
    device = "cpu"
    detector = SceneDescripter(kpt, device)
    
    # place pic to enable this test
    # scene_frame = cv2.imread("/home/aic/audio-accompaniment/pics/temp_pic.jpg")
    # scenes_backbones = detector.detect_backbones(scene_frame)
    # print(scenes_backbones)
    # scenes_descriptions = detector.get_scene_description(**scenes_backbones)
    # print(scenes_descriptions)
