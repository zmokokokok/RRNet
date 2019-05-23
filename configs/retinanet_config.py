from datasets.transforms import *
from torch.utils.data import DistributedSampler
from easydict import EasyDict as edict


# Base Config ============================================
Config = edict()
Config.seed = 219
Config.dataset = 'drones_det'
Config.data_root = './data/DronesDET'
Config.log_prefix = 'RetinaNet'
Config.use_tensorboard = True
Config.num_classes = 10

# Training Config =========================================
Config.Train = edict()
# If use the pretrained backbone model.
Config.Train.pretrained = True

# Dataloader params.
Config.Train.batch_size = 8
Config.Train.num_workers = 4
Config.Train.sampler = DistributedSampler

# Optimizer params.
Config.Train.lr = 0.01
Config.Train.momentum = 0.9
Config.Train.weight_decay = 0.0001
# Milestones for changing learning rage.
Config.Train.lr_milestones = [60000, 80000]

Config.Train.iter_num = 90000

# Transforms
Config.Train.crop_size = (512, 512)
Config.Train.mean = (0.485, 0.456, 0.406)
Config.Train.std = (0.229, 0.224, 0.225)
Config.Train.transforms = Compose([
    ToTensor(),
    HorizontalFlip(),
    RandomCrop(Config.Train.crop_size),
    Normalize(Config.Train.mean, Config.Train.std)
])

# Log params.
Config.Train.print_interval = 20
Config.Train.checkpoint_interval = 30000


# Validation Config =========================================
Config.Val = edict()
Config.Val.model_path = './log/model.pth'

# Dataloader params.
Config.Val.batch_size = 2
Config.Val.num_workers = 4
Config.Val.sampler = DistributedSampler

# Transforms
Config.Val.mean = (0.485, 0.456, 0.406)
Config.Val.std = (0.229, 0.224, 0.225)
Config.Val.transforms = Compose([
    ToTensor(),
    Normalize(Config.Val.mean, Config.Val.std)
])


# Model Config ===============================================
Config.Model = edict()
Config.Model.backbone = 'resnet50'
Config.Model.fpn = 'fpn'
Config.Model.cls_detector = 'retinanet_detector'
Config.Model.loc_detector = 'retinanet_detector'
Config.Model.num_anchors = 9


# Distributed Config =========================================
Config.Distributed = edict()
Config.Distributed.world_size = 1
Config.Distributed.gpu_id = -1
Config.Distributed.rank = 0
Config.Distributed.ngpus_per_node = 1
Config.Distributed.dist_url = 'tcp://127.0.0.1:34567'
