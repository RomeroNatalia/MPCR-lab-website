---
layout: poster-template
title: "Emergent Communication in Multi-Agent Swarm Systems: From Local Interaction to Global Coordination"
orientation: vertical
presenters:
  - name: "Natalia Romero"
    affiliation: "1"
  - name: "William E. Hahn"
    affiliation: "1"
  - name: "Elan Barenholtz"
    affiliation: "1"
advisor: "Elan Barenholtz, Ph.D."
department: "Machine Perception and Cognitive Robotics Laboratory"
institution: "Florida Atlantic University, Boca Raton, FL"
contact_email: "mpcrlab@fau.edu"
project_url: "https://mpcrlab.com/projects/"
acknowledgments: "Supported by Florida Atlantic University. Simulations conducted using the FAU HPC cluster. The authors thank the MPCR Lab members for feedback during development."

sections:
  - title: "Introduction"
    content: |
      Swarm intelligence emerges from simple local rules governing individual agents, yet produces sophisticated collective behaviors observed in nature -- flocking, foraging, and distributed decision-making.

      **Central Question:** Can artificial swarm agents evolve communication protocols that enable efficient global coordination without centralized control?

      We explore how reinforcement learning agents in a multi-agent environment develop emergent signaling behaviors, studying the structure and efficiency of the resulting communication channels.

      #### Objectives
      - Design a multi-agent environment requiring coordination for task success
      - Analyze emergent communication protocols for compositionality
      - Compare evolved protocols against hand-designed baselines
      - Measure information-theoretic properties of agent signals

  - title: "Background"
    accent: "accent-electric"
    content: |
      #### Biological Inspiration

      Social insects (ants, bees) use stigmergic communication -- modifying the environment to convey information indirectly. Honey bees perform waggle dances encoding distance and direction to food sources with remarkable precision.

      #### Computational Approaches

      **Multi-Agent Reinforcement Learning (MARL)** provides a framework for studying emergent communication. Key architectures include:

      - **DIAL** (Foerster et al., 2016): Differentiable inter-agent learning with continuous channels
      - **CommNet** (Sukhbaatar et al., 2016): Mean-field communication averaging
      - **TarMAC** (Das et al., 2019): Targeted multi-agent communication with attention

      #### Gap in Literature
      Prior work focuses on discrete message passing. We investigate continuous signal spaces that better model biological communication channels.

  - title: "Methods"
    content: |
      #### Environment Design

      We implement a **foraging task** in a 2D continuous space with:
      - *N* = 16 agents with limited sensing radius (*r* = 0.15)
      - *K* = 5 resource patches with varying reward values
      - Episode length: 500 timesteps
      - Agents observe local neighbors and their signal vectors

      #### Agent Architecture

      Each agent has three neural modules:

      **Perception Network:** Encodes local observations (nearby agents, resources, obstacles) into a 64-dim feature vector.

      **Communication Network:** Produces a continuous signal vector *s* in R^8 broadcast to neighbors within communication range *r_c* = 0.3.

      **Policy Network:** Maps perception features + received signals to actions (velocity, heading) using PPO with shared parameters.

      #### Training Protocol
      - 10M environment steps with curriculum (increasing *K* over training)
      - Population-based training with 8 parallel populations
      - Mutual information regularization on signal channels

  - title: "Results"
    accent: "accent-red"
    content: |
      #### Coordination Performance

      | Method | Resources Found | Avg. Steps | Collisions |
      |--------|----------------|-----------|------------|
      | No Communication | 2.1 / 5 | 380 | 45.2 |
      | Random Signals | 2.3 / 5 | 365 | 42.8 |
      | Hand-designed | 3.8 / 5 | 210 | 12.1 |
      | Emergent (Ours) | **4.4 / 5** | **165** | **8.7** |

      #### Emergent Protocol Analysis
      - Agents develop **3 distinct signal modes** corresponding to: resource discovery, danger avoidance, and group formation
      - Mutual information between signals and environmental states: **I(S;E) = 2.34 bits** (vs. 0.12 for random)
      - Signal compositionality score: **0.72** (topographic similarity metric)
      - Protocol is **robust to 20% agent failure** -- remaining agents maintain 85% coordination efficiency

  - title: "Discussion"
    accent: "accent-stone"
    content: |
      The emergent protocols exhibit several properties analogous to biological communication:

      **Graded Signaling:** Signal magnitude correlates with resource value (r = 0.89), similar to honeybee waggle dance duration encoding distance.

      **Contextual Interpretation:** The same signal is interpreted differently based on the receiver's state, demonstrating pragmatic communication.

      **Redundancy:** Agents evolve partially redundant channels, providing fault tolerance without explicit design.

      These findings support the hypothesis that communication structure is shaped primarily by task demands and physical constraints, not agent complexity.

  - title: "Conclusion"
    accent: "accent-red"
    content: |
      We demonstrate that multi-agent swarms can evolve structured, efficient communication protocols through reinforcement learning that **outperform hand-designed baselines** by 16% on resource discovery tasks.

      #### Key Contributions
      - Continuous-signal multi-agent communication framework
      - Evidence for spontaneous compositionality in emergent protocols
      - Information-theoretic analysis toolkit for agent communication
      - Open-source environment for swarm communication research

      #### Future Directions
      - Transfer learned protocols to physical robot swarms
      - Scale to 100+ agent populations
      - Investigate language grounding from emergent signals

  - title: "References"
    accent: "accent-dark"
    content: |
      1. Foerster, J., et al. (2016). Learning to communicate with deep multi-agent reinforcement learning. *NeurIPS 2016*.

      2. Sukhbaatar, S., Szlam, A., & Fergus, R. (2016). Learning multiagent communication with backpropagation. *NeurIPS 2016*.

      3. Das, A., et al. (2019). TarMAC: Targeted multi-agent communication. *ICML 2019*.

      4. Lazaridou, A., et al. (2017). Multi-agent cooperation and the emergence of (natural) language. *ICLR 2017*.

      5. Mordatch, I., & Abbeel, P. (2018). Emergence of grounded compositional language in multi-agent populations. *AAAI 2018*.

images:
  - title: "Agent Architecture"
    placeholder: "Insert agent neural architecture diagram here"
    caption: "Figure 1. Three-module agent architecture: perception encoder, communication network, and policy network with PPO training."

  - title: "Emergent Signal Analysis"
    placeholder: "Insert t-SNE visualization of signal space here"
    caption: "Figure 2. t-SNE projection of agent signals colored by environmental context. Three distinct clusters correspond to resource, danger, and grouping signals."
---
