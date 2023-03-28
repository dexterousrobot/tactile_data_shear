import os

from tactile_data_john.tactile_servo_control import BASE_DATA_PATH
from tactile_data_john.utils_data import load_pkl_obj, save_json_obj


file_path = os.path.join(BASE_DATA_PATH, 'franka_tactip_2', 'surface_3d', 'val', 'meta')

meta_dict = load_pkl_obj(file_path)

del meta_dict['root_dir'], meta_dict['data_dir'], meta_dict['image_target_file'], meta_dict['image_dir']
print(meta_dict)

save_json_obj(meta_dict, file_path)
