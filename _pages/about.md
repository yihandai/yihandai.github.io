---
permalink: /
title: "Yihan Dai 代易函"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
layout: archive
---

I am a first year Master student at the [Institute of Software, Chinese Academy of Sciences (ISCAS)](http://www.iscas.ac.cn). Before that, I got my Bachelor degree at [Wuhan University of Technology](https://www.whut.edu.cn). My research interests lie in reinforcement learning, VLN and explainable AI. I am passionate about developing reliable and efficient agents.

## Publications

<video playsinline autoplay loop muted 
       src="images/hat/hat_demo.mp4" 
       poster="./images/loading-icon.gif" 
       alt="sym" width="45%" 
       style="border-radius:15px; float:left; margin-right:15px;">
</video>

### [Humanoid Policy ~ Human Policy](https://human-as-robot.github.io/)

**Authors:** Ri-Zhao Qiu\*, Shiqi Yang\*, Xuxin Cheng\*, Chaitanya Chawla,  
Jialong Li, Tairan He, Ge Yan, David J. Yoon, Ryan Hoque, Lars Paulsen,  
Ge Yang, Jian Zhang, Sha Yi, Guanya Shi, Xiaolong Wang  
**Year:** 2025

[Webpage](https://human-as-robot.github.io/) | 
[PDF](https://arxiv.org/pdf/2503.13441) | 
[Abstract](#hat-abstract) | 
[BibTeX](#hat-bibtex) | 
[arXiv](https://arxiv.org/abs/2503.13441) | 
[Code](https://github.com/RogerQi/human-policy)

<a id="hat-abstract"></a>
*Training manipulation policies for humanoid robots with diverse data enhance their robustness and generalization across tasks and platforms. However, learning solely from robot demonstrations is labor-intensive, requiring expensive tele-operated data collection which is difficult to scale. This paper investigates a more scalable data source, egocentric human demonstrations, to serve as cross-embodiment training data for robot learning. We mitigate the embodiment gap between humanoids and humans from both the data and modeling perspectives. We collect an egocentric task-oriented dataset (PH2D) that is directly aligned with humanoid manipulation demonstrations. We then train a human-humanoid behavior policy, which we term Human Action Transformer (HAT). The state-action space of HAT is unified for both humans and humanoid robots and can be differentiably retargeted to robot actions. Co-trained with smaller-scale robot data, HAT directly models humanoid robots and humans as different embodiments without additional supervision. We show that human data improves both generalization and robustness of HAT with significantly better data collection efficiency.*

<a id="hat-bibtex"></a>
```bibtex
@article{qiu2025-humanpolicy,
  title={Humanoid Policy \~{} Human Policy},
  author={Ri-Zhao Qiu and Shiqi Yang and Xuxin Cheng and Chaitanya Chawla and Jialong Li and Tairan He and Ge Yan and David J. Yoon and Ryan Hoque and Lars Paulsen and Ge Yang and Jian Zhang and Sha Yi and Guanya Shi and Xiaolong Wang},
  journal={arXiv preprint arXiv:2503.13441},
  year={2025}
}
