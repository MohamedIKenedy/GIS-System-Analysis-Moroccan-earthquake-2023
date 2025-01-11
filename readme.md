# Machine Learning-Based Earthquake Damage Assessment

## Overview
This project provides a comprehensive machine learning pipeline for analyzing satellite imagery to assess earthquake damage. Using Maxar Open Data satellite imagery from the 2023 Morocco Earthquake, the system combines multiple deep learning models to detect buildings, identify changes, and classify damage levels.

## Features
- Building footprint detection using U-Net architecture
- Change detection between pre- and post-earthquake imagery using Siamese networks
- Damage level classification using ResNet-50
- Automated batch processing of multiple image pairs
- Interactive visualization of results using leafmap
- Complete data preprocessing pipeline

## Requirements
- Python 3.8+
- PyTorch 1.9+
- CUDA-capable GPU (recommended)

### Dependencies
```bash
pip install -r requirements.txt
```

Core dependencies include:
- leafmap
- geopandas
- cogeo-mosaic
- torch
- torchvision
- segmentation-models-pytorch
- rasterio
- numpy
- pandas
- scikit-learn
- opencv-python

## Installation
1. Clone the repository:
```bash
git clone https://github.com/MohamedIKenedy/GIS-System-Analysis-Moroccan-earthquake-2023.git
cd GIS-System-Analysis-Moroccan-earthquake-2023
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```


## Usage

### Quick Start
1. Open the Jupyter notebook:
```bash
jupyter notebook morocco_earthquake_ml.ipynb
```

2. Follow the notebook cells to:
   - Load and preprocess satellite imagery
   - Run building detection
   - Perform change detection
   - Classify damage levels
   - Visualize results

### Running Batch Analysis
```python
from earthquake_analysis import batch_analyze_region

# Prepare image lists
before_images = ["url1", "url2", ...]
after_images = ["url1", "url2", ...]

# Run analysis
results_df = batch_analyze_region(before_images, after_images)
```

## Model Architecture

### Building Detection
- Architecture: U-Net with ResNet-34 encoder
- Input: RGB satellite imagery (512x512)
- Output: Building footprint mask

### Change Detection
- Architecture: Siamese network with ResNet-34 backbone
- Input: Pair of before/after images
- Output: Change probability score

### Damage Classification
- Architecture: ResNet-50
- Input: RGB satellite imagery (512x512)
- Output: 4-class damage level classification
  - No Damage
  - Minor Damage
  - Major Damage
  - Destroyed

## Data Format
Input imagery should be:
- GeoTIFF format
- RGB channels
- High resolution (preferably sub-meter)
- Orthorectified and aligned

## Performance Considerations
- GPU with at least 8GB VRAM recommended
- Batch size may need adjustment based on available memory
- Processing time: ~2-3 seconds per image pair on modern GPU

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Training Your Own Models
To train models on your own data:
1. Prepare training data in the following format:
   ```
   data/
   ├── buildings/
   │   ├── images/
   │   └── masks/
   ├── changes/
   │   ├── before/
   │   └── after/
   └── damage/
       ├── no_damage/
       ├── minor/
       ├── major/
       └── destroyed/
   ```

2. Run training scripts:
   ```bash
   python train_building_detector.py --data-path data/buildings
   python train_change_detector.py --data-path data/changes
   python train_damage_classifier.py --data-path data/damage
   ```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Maxar Open Data Program for providing satellite imagery
- leafmap developers for the visualization framework
- Humanitarian OpenStreetMap Team for building footprint data



## Contact
For questions and support, please open an issue in the GitHub repository or contact [your@email.com](mailto:your@email.com).
