# 🚦 NH-53 Safety Monitor  
### Accident Hotspot Identification & Predictive Simulation System

An Intelligent Transportation System (ITS) project focused on identifying accident-prone zones (hotspots) along **NH-53** using spatial clustering and severity analysis.

The system combines **DBSCAN clustering, geospatial visualization, and a real-time simulation prototype** to support proactive road safety planning.

---

## 🌐 System Overview

The project is built around three major components:

1. **Hotspot Analytics Dashboard**
2. **Interactive Map Visualization**
3. **Real-Time Driving Simulation Prototype**

---

# 🖥️ Command Center Interface

![NH-53 Command Center](images/command_center.png)

The main control panel provides:

- Access to hotspot analytics
- Launch simulation module
- Operational system status
- Data stream monitoring (2020–2024)
- Version control & system state

This serves as the central gateway for analytics and simulation features.

---

# 🗺️ Hotspot Analytics Dashboard

![Hotspot Analytics](images/hotspot_analytics.png)

An interactive geospatial dashboard built using:

- Leaflet.js  
- OpenStreetMap  
- GeoJSON outputs from DBSCAN  

### Features:

- 🔴 Critical Hotspots  
- 🟠 Serious Hotspots  
- 🟡 Moderate Hotspots  
- Severity-based filtering  
- Deep search (cause, weather, accident type)  
- Cluster-level inspection  
- Street View integration  

The dashboard identified:

- **983 accident records analyzed**
- **99 hotspot clusters detected**
- **504 isolated accidents (noise)**

---

# 🚗 Real-Time Simulation Prototype (Run-a-Car)

![Simulation Dashboard](images/simulation_dashboard.png)

A predictive simulation system that mimics real driving along NH-53.

### Key Capabilities:

- Continuous route playback  
- Adjustable simulation speed  
- Configurable alert radius  
- Audio + visual hotspot alerts  
- Color-coded severity warnings  
- Real-time telemetry log  

When approaching a hotspot, the system triggers:

- ⚠️ Pre-alert warning  
- 🎯 Severity-based notification  
- 📢 Recommended speed guidance  

This demonstrates how hotspot intelligence can be integrated into smart transportation systems.

---

# 🧠 Methodology

### Data Source
- NH-53 accident data (2020–2024)
- 983 cleaned and merged records

### Clustering Algorithm
- **DBSCAN (Density-Based Spatial Clustering)**
- `eps = 100 meters`
- `min_samples = 3`

The algorithm detects dense accident regions and filters isolated incidents.

---

## 🚨 Severity Classification

Severity Score Formula:

Score = (4 × Fatal) + (3 × Grievous) + (1.5 × Minor) + (0.5 × Non-Injury)

Hotspots are categorized as:

- 🔴 Critical  
- 🟠 Serious  
- 🟡 Moderate  

This classification helps prioritize safety interventions.

---

# 🏗️ System Workflow

1. Accident Data Collection (2020–2024)  
2. Data Cleaning & Coordinate Standardization  
3. DBSCAN Clustering (Python)  
4. Severity Score Computation  
5. GeoJSON Generation  
6. Web-Based Visualization  
7. Simulation Integration  

---

# 📊 Key Observations

- Overspeeding and Driver Fault were dominant causes  
- Skidding and Head-on collisions were frequent accident types  
- Most incidents occurred on straight road segments  
- Majority of accidents occurred during clear weather  

---

# 🛠️ Tech Stack

| Component | Technology |
|------------|------------|
| Data Processing | Python |
| Clustering | DBSCAN |
| Mapping | Leaflet.js |
| Map Tiles | OpenStreetMap |
| Data Format | GeoJSON |
| Simulation UI | HTML, CSS, JavaScript |

---

# 🚀 Future Enhancements

- Real-time accident data integration  
- Time-based hotspot prediction  
- ML-based accident risk forecasting  
- Integration with emergency alert systems  
- Public safety deployment for traffic authorities  

---

# 👨‍💻 Contributors

- Pradeep Kumar  
- Harphool Singh  
- Guided by: Dr. Shriniwas Arkatkar  

---

# 🎯 Conclusion

The NH-53 Safety Monitor demonstrates how spatial clustering, severity modeling, and geospatial visualization can be combined to identify accident hotspots and enable predictive safety simulation.

This project bridges AI, GIS, and Intelligent Transportation Systems to support data-driven road safety decisions.
