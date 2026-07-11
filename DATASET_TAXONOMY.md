# Dataset Taxonomy

This file defines the canonical fields and controlled values for the dataset
summary table. The same fields should appear in the main repository table and
in each individual dataset page. Longer notes, caveats, sensor details, split
descriptions, and citations should stay in the dataset description and
references.

## General Rules

- Use the exact field names and controlled values from this file.
- Use semicolon-separated values for multi-value fields.
- Prefer 1 to 3 values per multi-value field. Add more only when they materially
  improve filtering.
- Prefer specific, searchable values over broad wording.
- Use `Information not available` only after checking the source.
- Do not use near-synonyms. If a new value is needed, add it here first.
- Keep `Size` short and human-readable rather than forcing every dataset into
  the same unit.

## Canonical Table Fields

| Field | Type | Required | Values / Format | Purpose |
| --- | --- | --- | --- | --- |
| `Dataset` | Text | Yes | Official or commonly used dataset name | Human-readable identifier and link target. |
| `Domain` | Controlled multi-value | Yes | See [Domain](#domain) | Broad industrial area, useful for first-pass filtering. |
| `Asset / Process` | Controlled-light multi-value | Yes | See [Asset / Process](#asset--process) | Concrete equipment, product, material, or process covered by the dataset. |
| `Modality` | Controlled multi-value | Yes | See [Modality](#modality) | What kind of data the user will actually work with. |
| `Task` | Controlled multi-value | Yes | See [Task](#task) | Main ML, analytics, or benchmarking tasks supported by the dataset. |
| `Annotation` | Controlled multi-value | Yes | See [Annotation](#annotation) | What ground truth or labels are available, with more detail than a yes/no label. |
| `Source Type` | Controlled single-value | Yes | See [Source Type](#source-type) | How realistic the data origin is and whether it is simulated, synthetic, or collected from real systems. |
| `Access` | Controlled multi-value | Yes | See [Access](#access) | How a user can obtain the data and how much friction to expect. |
| `Size` | Short text | Recommended | Examples: `150k images`, `18 runs`, `847 parts`, `4.4k records`, `53 GB` | Quick sense of scale, adapted to the modality. |
| `Year` | Year or text | Recommended | `YYYY`, `YYYY-YYYY`, or `Information not available` | Release year, donation year, or paper year, in that order of preference. |
| `License` | Controlled value plus version if known | Recommended | See [License](#license) | Reuse constraints and commercial/non-commercial expectations. |

## Domain

Use `Domain` for the broad industrial sector or application area. It can be
multi-valued when the dataset genuinely spans sectors.

| Value | Use For |
| --- | --- |
| `Manufacturing & Production` | Generic factory, assembly, machining, production-line, quality-control, and Industry 4.0 datasets. |
| `Electronics & Semiconductor` | PCB, wafer, chip, electronics assembly, and semiconductor manufacturing datasets. |
| `Energy & Power` | Power generation, power grids, electricity consumption, renewable energy, turbines, and energy optimization. |
| `Oil & Gas` | Oil wells, drilling, production, petroleum operations, refineries, and oil/gas economics. |
| `Chemical & Process` | Chemical plants, process control, fermentation, cement, gas sensors, and continuous/batch process industries. |
| `Water & Utilities` | Water treatment, water distribution, utility operations, and water SCADA systems. |
| `Robotics & Automation` | Robotic manipulation, industrial robots, pick-and-place, warehouse automation, and robot execution datasets. |
| `Aerospace & Defense` | Aircraft, turbofan engines, aerospace inspection, defense manufacturers, and military-industrial datasets. |
| `Transportation & Mobility` | Vehicles, railways, trucks, automotive manufacturing, fleet systems, and mobility infrastructure. |
| `Infrastructure & Civil` | Bridges, roads, buildings, civil structures, cracks, concrete, and structural health monitoring. |
| `Materials & Metrology` | Materials testing, surface metrology, ceramics, superconductors, textures, and high-precision measurement. |
| `Logistics & Retail` | Warehouses, retail items, packaging, supply-chain inspection, and logistics defect detection. |
| `Buildings & Appliances` | Smart homes, appliances, building energy, household electricity, and indoor environmental monitoring. |
| `Environment & Safety` | Air quality, emissions, industrial safety, occupational health, and environmental monitoring. |
| `Cyber-Physical Security` | Industrial control-system attacks, IIoT intrusion detection, SCADA security, and cyber-physical anomaly detection. |
| `Business & Economics` | Industrial reports, production statistics, prices, imports, company rankings, and economic indicators. |
| `General / Cross-Industrial` | Broad repositories, benchmark suites, or datasets intentionally spanning many industrial sectors. |

## Asset / Process

Use `Asset / Process` for the concrete object, equipment type, material, or
process. This field is controlled-light: prefer the values below, but new values
may be added when a dataset covers a specific asset not listed here.

| Preferred Value | Use For |
| --- | --- |
| `General Manufacturing` | Broad production datasets without one dominant asset. |
| `Surface Defects` | Generic surface inspection where material or product is not the main filter. |
| `Bearings` | Bearing vibration, degradation, fault diagnosis, and RUL datasets. |
| `Gears / Gearboxes` | Gear or gearbox condition-monitoring datasets. |
| `Motors / Drives` | Electric motors, drives, brushless motors, and motor-current datasets. |
| `Pumps` | Pump sensors, pump faults, and pumping-system datasets. |
| `Valves / Actuators` | Valve stiction, actuators, control valves, and related control-loop datasets. |
| `Turbines / Engines` | Turbofan, diesel, naval propulsion, wind turbines, and engine degradation datasets. |
| `CNC / Machining` | CNC milling, turning, chatter, tool wear, and tool-path datasets. |
| `Welding` | TIG, laser welding, weld defects, and weld quality datasets. |
| `Additive Manufacturing` | 3D printing, additive manufacturing scans, and printed-part quality datasets. |
| `Casting / Metal Parts` | Casting products, metal parts, machined parts, and metallic defect datasets. |
| `Steel / Metal Surfaces` | Steel plates, steel strips, metal surface defects, and steel industry inspection. |
| `PCB / Electronics` | PCB defects, electronic products, 3C products, and electronics assembly. |
| `Semiconductor / Wafers` | Wafer maps, wafer manufacturing, SECOM-style semiconductor process data. |
| `Batteries` | Li-ion cells, battery aging, battery cycle life, and battery diagnostics. |
| `Solar / PV` | Solar cells, photovoltaic defects, solar generation, and PV plant data. |
| `Power Grid / Plants` | Power plants, grid stability, power consumption, and generation datasets. |
| `Vehicles / Fleets` | Vehicles, trucks, automotive manufacturing, fleets, vehicle evaluation, and mobility assets. |
| `Water Treatment / Distribution` | Water process, water distribution, and utility SCADA datasets. |
| `Chemical Process` | Tennessee Eastman, fermentation, cement, gas sensors, and process-control data. |
| `Oil Wells / Reservoirs` | Oil wells, oil sands, well logs, drilling, and reservoir data. |
| `SCADA / ICS` | Industrial control systems, IIoT, network telemetry, and cyber-physical systems. |
| `Robotic Manipulation` | Robot execution, pick-and-place, robotic observation, and industrial manipulation. |
| `Industrial Machines` | Generic machines, fans, pumps, sliders, valves, toy machines, and machine operating sounds when no single equipment class dominates. |
| `Textile / Apparel` | Fabric defects, garments, textile production, and apparel productivity. |
| `Retail / Logistics Items` | Retail goods, packaging, warehouse items, and logistics inspection datasets. |
| `Buildings / Appliances` | Appliances, smart homes, building energy, and indoor sensor datasets. |
| `Infrastructure Cracks` | Roads, bridges, concrete cracks, and civil infrastructure visual inspection. |
| `Materials / Chemistry` | Ceramics, superconductors, materials composition, and material-property datasets. |
| `Business / Economic Indicators` | Prices, imports, rankings, public records, and industry reports. |
| `Other / Cross-Domain` | Use only when no more specific value fits. |

## Modality

Use `Modality` for the data format or sensor family. This field is multi-value.

| Value | Use For |
| --- | --- |
| `Tabular` | Rows and columns without inherent temporal ordering. |
| `Time Series` | Ordered sensor data, SCADA data, logs, run-to-failure data, or repeated measurements over time. |
| `Image` | RGB, grayscale, microscopy, surface images, or standard 2D visual inspection images. |
| `Video` | Ordered image sequences, surveillance, inspection videos, or egocentric video. |
| `Audio` | Sound, acoustic emission, machine operating sound, or microphone data. |
| `Vibration` | Accelerometer and vibration-specific signals where vibration is central to the dataset. |
| `3D Point Cloud` | Point-cloud, PLY, PCD, or geometry-first 3D datasets. |
| `RGB-D` | Paired RGB and depth data. |
| `X-ray / CT` | X-ray, CT, or other non-destructive radiographic imaging. |
| `Geospatial / Remote Sensing` | Satellite, aerial, map, or geospatially indexed data. |
| `Network Traffic` | PCAP, flow logs, intrusion data, or communication telemetry. |
| `Text / Documents` | Text records, reports, QA labels, documentation, or language annotations. |
| `Multimodal` | Dataset intentionally combines multiple modalities as part of its benchmark design. Use alongside the concrete modalities when possible. |

## Task

Use `Task` for the main research or applied tasks. This field is multi-value.
Prefer the most specific task available.

| Value | Use For |
| --- | --- |
| `Anomaly Detection` | Detecting abnormal samples, events, patterns, or states. |
| `Anomaly Localization` | Locating anomalous regions without necessarily classifying defect type. |
| `Defect Detection` | Detecting manufacturing or visual defects, especially in inspection settings. |
| `Defect Segmentation` | Pixel-level, instance-level, or point-level defect segmentation. |
| `Object Detection` | Bounding-box or object-presence detection. |
| `Classification` | General class prediction when a more specific task is not enough. |
| `Regression` | Continuous-value prediction when a more specific target is not enough. |
| `Quality Prediction` | Predicting product quality, yield, pass/fail, or process outcome. |
| `Fault Diagnosis` | Identifying fault state, fault type, fault component, or failure mode. |
| `Failure Prediction` | Predicting whether or when a failure will occur. |
| `RUL / Prognostics` | Remaining useful life, degradation modelling, and run-to-failure prediction. |
| `Predictive Maintenance` | Maintenance-oriented prediction or maintenance decision support. |
| `Condition Monitoring` | Monitoring equipment health from sensors, audio, vibration, or process signals. |
| `Process Monitoring` | Monitoring process variables, control loops, or industrial operating states. |
| `Forecasting` | Predicting future demand, production, energy, sensor values, or prices. |
| `Energy Optimization` | Optimizing or analysing energy consumption, efficiency, or load. |
| `Cyberattack Detection` | Detecting attacks on SCADA, ICS, water systems, IIoT, or cyber-physical systems. |
| `Intrusion Detection` | Network or IIoT intrusion detection from traffic or telemetry. |
| `Pose Estimation` | 6D pose, object pose, orientation, or geometric pose estimation. |
| `3D Understanding` | 3D recognition, reconstruction, 3D inspection, or geometry-aware learning. |
| `Simulation / Control` | Control-system simulation, process control, or control-loop evaluation. |
| `Recommendation / Decision Support` | Maintenance action recommendation, operational planning, or agentic workflows. |
| `Benchmark Suite` | Meta-benchmarks or collections designed to evaluate several tasks. |

## Annotation

Use `Annotation` for the available ground truth. This field is multi-value and
should be more informative than a simple yes/no label.

| Value | Use For |
| --- | --- |
| `Unlabeled` | No labels or ground truth; useful for unsupervised exploration. |
| `Normal-Only Training` | Training split contains only normal samples, common in anomaly detection. |
| `Sample Label` | Each sample has a normal/anomalous, pass/fail, or class label. |
| `Class Label` | General categorical class labels. |
| `Fault Type Label` | Labels identify fault mode, defect type, failure type, or attack type. |
| `Time / Event Label` | Labels mark event windows, attack intervals, fault times, or change points. |
| `RUL Label` | Remaining useful life, cycle-to-failure, or degradation target. |
| `Scalar Target` | Continuous regression target such as quality score, strength, energy, cost, or temperature. |
| `Bounding Box` | Object or defect bounding boxes. |
| `Pixel Mask` | Pixel-level masks for defects, objects, anomalies, or segments. |
| `Instance Mask` | Instance-level segmentation masks. |
| `3D / Point Mask` | Point-level, mesh-level, or 3D geometric anomaly masks. |
| `Pose / Keypoint Label` | Pose, orientation, 6D pose, or keypoint annotations. |
| `Text / QA Label` | Text descriptions, visual question answering, prompts, or language supervision. |
| `Split Metadata` | Official train/test splits or metadata without detailed labels. |
| `Partial` | Only some samples, splits, or categories have labels. |
| `Mixed` | Multiple annotation types are central to the dataset. Use alongside concrete values where possible. |

## Source Type

Use `Source Type` for the origin of the data. This field should usually have
one value. Use `Mixed` when multiple origins are essential to the dataset.

| Value | Use For |
| --- | --- |
| `Real Production / Field` | Collected from real operating assets, production lines, field equipment, or deployed systems. |
| `Real Lab / Testbed` | Collected from physical rigs, labs, pilots, testbeds, or controlled acquisition setups. |
| `Simulation` | Generated by a physics, process, plant, or system simulator. |
| `Synthetic` | Artificially generated data not primarily based on a mechanistic simulator. |
| `Mixed` | Meaningful combination of real, synthetic, simulation, or testbed data. |
| `Public Records` | Official statistics, public reports, prices, imports, emissions, or economic records. |
| `Remote Sensing` | Satellite, aerial, or geospatial observations of industrial assets. |
| `Derived / Aggregated` | Repackaged, cleaned, combined, or benchmarked from other public datasets. |
| `Information not available` | Source cannot be determined from available references. |

## Access

Use `Access` for both access platform and access friction. This field is
multi-value because platform and friction are often both useful.

| Value | Use For |
| --- | --- |
| `Direct Download` | Files can be downloaded directly from the linked page. |
| `Repository` | Dataset is hosted or linked from GitHub, GitLab, or another code repository. |
| `Official Portal` | Dataset is hosted by a university, lab, company, government, NASA, UCI, PHM Society, or similar official page. |
| `UCI` | Access through the UCI Machine Learning Repository. |
| `Mendeley Data` | Access through Mendeley Data. |
| `IEEE DataPort` | Access through IEEE DataPort. |
| `Kaggle` | Access through Kaggle dataset or competition pages. |
| `Hugging Face` | Access through Hugging Face datasets, papers, or model/data pages. |
| `Zenodo / Dataverse` | Access through Zenodo, Harvard Dataverse, or similar archival repositories. |
| `Competition` | Data access is tied to a challenge or competition. |
| `Form Request` | User must submit a request form or contact maintainers. |
| `Gated Approval` | Access requires approval, acceptance of terms, or account-based gating. |
| `Login Required` | Account is required, but approval is not necessarily required. |
| `Restricted / Non-Public` | Dataset is described publicly but data is not openly available. |
| `Unavailable / Broken` | Link or access path is no longer usable. |
| `Information not available` | Access path cannot be confirmed. |

## License

Use the exact license version when known. If license terms are not a standard
open-source or Creative Commons license, use the nearest controlled value and
explain details in the description.

| Value | Use For |
| --- | --- |
| `CC0` | Public-domain dedication or CC0 datasets. |
| `CC BY` | Creative Commons Attribution, with version if known. |
| `CC BY-SA` | Creative Commons Attribution-ShareAlike, with version if known. |
| `CC BY-NC` | Creative Commons Attribution-NonCommercial, with version if known. |
| `CC BY-NC-SA` | Creative Commons Attribution-NonCommercial-ShareAlike, with version if known. |
| `MIT` | MIT-licensed code/data repository. |
| `Apache-2.0` | Apache License 2.0. |
| `GPL` | GPL-family license. Include version if known. |
| `ODC / Open Data Commons` | ODbL, ODC-BY, or related Open Data Commons licenses. |
| `Custom Research` | Custom terms intended mainly for research use. |
| `Academic / Non-Commercial` | Explicit academic-only or non-commercial research terms. |
| `Competition Terms` | Kaggle or challenge-specific rules govern data use. |
| `Proprietary / Restricted` | Proprietary, private, or explicitly restricted terms. |
| `Information not available` | No license or reuse terms found. |

## Size Formatting

`Size` is intentionally not a strict enum. Use the unit that helps a user
understand scale fastest.

| Modality / Dataset Type | Preferred Size Format |
| --- | --- |
| Image | `N images`, optionally with categories or masks. |
| Video | `N videos` or `N clips`. |
| Audio | `N clips`, `N hours`, or `N recordings`. |
| Time Series | `N runs`, `N time steps`, `N records`, `N sensors`, or `N assets`. |
| Tabular | `N rows`, `N records`, or `N instances`. |
| 3D / RGB-D | `N scans`, `N point clouds`, `N objects`, or `N views`. |
| Process / Testbed | `N runs`, `N batches`, `N scenarios`, or `N events`. |
| Repository / Benchmark Suite | `N datasets`, `N scenarios`, or `N tasks`. |
| Large Files | Add storage size when helpful, for example `150k images; 53 GB`. |

## Example Rows

| Dataset | Domain | Asset / Process | Modality | Task | Annotation | Source Type | Access | Size | Year | License |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `3D-ADAM` | `Manufacturing & Production` | `Additive Manufacturing` | `Image; RGB-D; 3D Point Cloud` | `Anomaly Detection; Defect Segmentation` | `Sample Label; Pixel Mask; 3D / Point Mask` | `Real Lab / Testbed` | `Hugging Face` | `14.1k 3D scans; 27.3k defects` | `2025` | `Information not available` |
| `SWaT` | `Water & Utilities; Cyber-Physical Security` | `Water Treatment / Distribution; SCADA / ICS` | `Time Series` | `Cyberattack Detection; Anomaly Detection; Process Monitoring` | `Time / Event Label; Fault Type Label` | `Real Lab / Testbed` | `Form Request; Gated Approval` | `Information not available` | `Information not available` | `Custom Research` |
| `MVTec AD` | `Manufacturing & Production` | `Surface Defects` | `Image` | `Anomaly Detection; Anomaly Localization; Defect Segmentation` | `Normal-Only Training; Sample Label; Pixel Mask` | `Real Lab / Testbed` | `Official Portal; Form Request` | `5k+ images` | `2019` | `Custom Research` |
