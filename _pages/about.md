---
permalink: /
title: "Yihan Dai 代易函"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
layout: archive
---

I am a second year Master student at the [Institute of Software, Chinese Academy of Sciences (ISCAS)](http://www.iscas.ac.cn), working under the supervision of [Junjie Wang](https://junjiewangiscas.github.io/). Before that, I got my Bachelor degree at [Wuhan University of Technology](https://www.whut.edu.cn). My research interests lie in large language models and interpretability, with a particular focus on understanding their internal mechanisms and building reliable, interpretable agents. I am currently applying for PhD positions in machine learning and large language models starting in 2028.

<p style="margin-top: 0.5em;">
  <a href="https://scholar.google.com/citations?user=evwzw60AAAAJ&hl=en" target="_blank" rel="noopener" style="text-decoration: none; color: inherit;">
    📊 <strong>Google Scholar</strong>: <span id="scholar-citedby">—</span> citations, h-index: <span id="scholar-hindex">—</span>, i10-index: <span id="scholar-i10">—</span>
  </a>
</p>

<script>
fetch('/scholar_stats.json')
  .then(r => r.json())
  .then(d => {
    document.getElementById('scholar-citedby').textContent = d.citedby;
    document.getElementById('scholar-hindex').textContent   = d.hindex;
    document.getElementById('scholar-i10').textContent      = d.i10index;
  })
  .catch(() => { /* leave placeholder on failure */ });
</script>

<style>
  .publication-item {
    display: flex;
    align-items: flex-start;
    gap: 20px;
    flex-wrap: nowrap;
    margin-bottom: 28px;
  }

  .publication-item__image {
    flex: 1;
    max-width: 40%;
  }

  .publication-item__image img {
    width: 100%;
    border-radius: 15px;
  }

  .publication-item__content {
    flex: 2;
  }

  @media screen and (max-width: 768px) {
    .publication-item {
      flex-direction: column;
    }

    .publication-item__image {
      max-width: 100%;
    }
  }
</style>

## Publications

<div class="publication-item">

  <!-- Left side -->
  <div class="publication-item__image">
    <img src="images/StaRNet-1.png" 
         alt="StaRNet framework">
  </div>

  <!-- Right side -->
  <div class="publication-item__content">
    <h3 style="margin-top: 0;">
      <a href="https://ieeexplore.ieee.org/document/11122427/">
        Motion-Consistent Representation Learning for UAV-Based Action Recognition
      </a>
    </h3>
    Wenxuan Liu*, Xian Zhong†, Yihan Dai*, Xuemei Jia, Zheng Wang, Shin’ichi Satoh<br />
    T-ITS 2025<br />
    <a href="https://ieeexplore.ieee.org/document/11122427/">Webpage</a><br />
  </div>
</div>

<div class="publication-item">

  <!-- Left side -->
  <div class="publication-item__image">
    <img src="images/acl_overview.png" 
         alt="DEFT overview">
  </div>

  <!-- Right side -->
  <div class="publication-item__content">
    <h3 style="margin-top: 0;">
      <a href="https://aclanthology.org/2026.acl-long.1363/">
        DEFT: Demystifying VLN Failures via a Unified Dual-View Explainability Framework for LLM-based Agents
      </a>
    </h3>
    Yawen Wang, Yihan Dai, Jianming Chen, Junjie Wang, Qing Wang<br />
    ACL 2026<br />
    <a href="https://aclanthology.org/2026.acl-long.1363/">Webpage</a><br />
  </div>
</div>

## Service

- Journal Reviewer: *Neurocomputing*
