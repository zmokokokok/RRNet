from backbones.resnet import resnet10, resnet50, resnet101
from modules.fpn import FPN
from modules.nas.fpn import NASFPN
from detectors.retinanet_detector import RetinaNetDetector


def get_backbone(backbone, pretrained=False):
    if backbone == 'resnet10':
        return resnet10(pretrained=pretrained)
    elif backbone == 'resnet50':
        return resnet50(pretrained=pretrained)
    elif backbone == 'resnet101':
        return resnet101(pretrained=pretrained)
    else:
        return resnet50(pretrained=pretrained)


def get_fpn(fp_name, cfg=None):
    if fp_name == 'fpn':
        return FPN()
    elif fp_name == 'nasfpn':
        return NASFPN(cfg)
    else:
        return FPN()


def get_detector(det_name, planes):
    if det_name == 'retinanet_detector':
        return RetinaNetDetector(planes)
    else:
        return RetinaNetDetector(planes)
