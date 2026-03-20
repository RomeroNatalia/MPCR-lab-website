---
layout: poster-template
title: "Compressed Inference: Efficient Neural Network Deployment on Resource-Constrained Edge Devices"
orientation: horizontal
presenters:
  - name: "Ganesh Shiwakoti"
    affiliation: "1"
  - name: "William E. Hahn"
    affiliation: "1"
  - name: "Elan Barenholtz"
    affiliation: "1"
advisor: "William E. Hahn, Ph.D."
department: "Machine Perception and Cognitive Robotics Laboratory"
institution: "Florida Atlantic University, Boca Raton, FL"
contact_email: "mpcrlab@fau.edu"
project_url: "https://mpcrlab.com/projects/"
acknowledgments: "This work was supported by Florida Atlantic University and the Charles E. Schmidt College of Science. Computing resources provided by the FAU High Performance Computing Center."

sections:
  - title: "Introduction"
    content: |
      Deep neural networks have achieved remarkable performance across vision, language, and decision-making tasks, but their computational demands present significant barriers to real-world deployment on edge devices.

      **Key Challenge:** Modern transformer-based models require billions of floating-point operations per inference, exceeding the capabilities of embedded processors, microcontrollers, and mobile GPUs.

      **Our Approach:** We investigate a unified compression pipeline combining quantization, structured pruning, and knowledge distillation to reduce model size and latency while preserving task accuracy.

      #### Research Questions
      - Can we achieve >10x compression with <2% accuracy loss?
      - How do compression techniques interact when applied jointly?
      - What are the Pareto-optimal tradeoffs for edge deployment?

  - title: "Background"
    accent: "accent-electric"
    content: |
      #### Model Compression Landscape

      **Quantization** reduces numerical precision from FP32 to INT8/INT4, cutting memory footprint by 4-8x. Post-training quantization (PTQ) requires no retraining but may degrade accuracy on sensitive layers.

      **Structured Pruning** removes entire channels or attention heads, yielding direct speedups on standard hardware without sparse-matrix support.

      **Knowledge Distillation** transfers learned representations from a large teacher to a compact student network, recovering accuracy lost through compression.

      #### Prior Work
      - Han et al. (2016): Deep Compression pipeline achieving 35-49x compression on AlexNet/VGGNet
      - Hinton et al. (2015): Knowledge distillation framework with soft targets
      - Jacob et al. (2018): Quantization-aware training for efficient integer-arithmetic inference

  - title: "Methods"
    accent: "accent-electric"
    content: |
      #### Compression Pipeline

      Our three-stage pipeline processes pretrained models through:

      **Stage 1 -- Sensitivity Analysis:** Layer-wise perturbation analysis identifies compression-sensitive layers. We compute Fisher information scores to rank layer importance.

      **Stage 2 -- Joint Compression:** We apply structured pruning (channel removal) followed by mixed-precision quantization. Critical layers retain FP16; non-critical layers use INT8 or INT4.

      **Stage 3 -- Recovery Distillation:** The compressed model is fine-tuned with a combined loss:

      *L = alpha * L_task + (1 - alpha) * L_KD*

      where L_KD uses temperature-scaled softmax outputs from the uncompressed teacher.

      #### Hardware Targets
      - NVIDIA Jetson Nano (128 CUDA cores, 4GB RAM)
      - Raspberry Pi 4 (ARM Cortex-A72, 4GB RAM)
      - STM32 Microcontroller (ARM Cortex-M7, 1MB RAM)

  - title: "Results"
    accent: "accent-red"
    content: |
      #### ImageNet Classification (ResNet-50)

      | Method | Top-1 Acc. | Size (MB) | Speedup |
      |--------|-----------|-----------|---------|
      | Baseline (FP32) | 76.1% | 97.5 | 1.0x |
      | INT8 Quantization | 75.8% | 24.4 | 3.2x |
      | Pruning (50%) | 74.9% | 48.8 | 1.9x |
      | Ours (Joint) | 75.4% | 11.2 | 8.7x |
      | Ours + Distillation | 75.9% | 11.2 | 8.7x |

      #### Key Findings
      - **8.7x compression** with only 0.2% accuracy drop after distillation recovery
      - Joint pruning + quantization outperforms either technique alone
      - Fisher-guided sensitivity analysis preserves critical early-layer features
      - INT4 quantization feasible for 60% of layers without accuracy impact

      #### Edge Deployment Latency

      | Device | Baseline | Compressed | Speedup |
      |--------|----------|------------|---------|
      | Jetson Nano | 142ms | 18ms | 7.9x |
      | Raspberry Pi 4 | 890ms | 108ms | 8.2x |

  - title: "Conclusion"
    accent: "accent-red"
    content: |
      We demonstrate that a unified compression pipeline combining structured pruning, mixed-precision quantization, and knowledge distillation achieves near-lossless compression ratios exceeding 8x on standard architectures.

      #### Key Contributions
      - **Fisher-guided layer sensitivity analysis** for principled compression allocation
      - **Joint optimization** of pruning ratios and quantization precision per layer
      - **Recovery distillation** protocol that restores 70% of compression-induced accuracy loss
      - **Validated edge deployment** on three hardware platforms with real-time inference

      #### Future Work
      - Extend pipeline to large language models (LLMs) and vision-language architectures
      - Investigate hardware-aware neural architecture search (NAS) for compression
      - Develop automated compression profiling tools for the MPCR research platform

  - title: "References"
    accent: "accent-dark"
    content: |
      1. Han, S., Mao, H., & Dally, W. J. (2016). Deep Compression: Compressing deep neural networks with pruning, trained quantization and Huffman coding. *ICLR 2016*.

      2. Hinton, G., Vinyals, O., & Dean, J. (2015). Distilling the knowledge in a neural network. *arXiv:1503.02531*.

      3. Jacob, B., et al. (2018). Quantization and training of neural networks for efficient integer-arithmetic-only inference. *CVPR 2018*.

      4. Frankle, J., & Carlin, M. (2019). The Lottery Ticket Hypothesis: Finding sparse, trainable neural networks. *ICLR 2019*.

      5. Polino, A., Pascanu, R., & Alistarh, D. (2018). Model compression via distillation and quantization. *ICLR 2018*.

images:
  - title: "System Architecture"
    placeholder: "Insert compression pipeline diagram here"
    caption: "Figure 1. Three-stage compression pipeline: sensitivity analysis, joint pruning + quantization, and recovery distillation."

  - title: "Performance Comparison"
    placeholder: "Insert accuracy vs. compression ratio plot here"
    caption: "Figure 2. Pareto frontier of accuracy vs. compression ratio across methods. Our joint approach (red) dominates single-technique baselines."
---
