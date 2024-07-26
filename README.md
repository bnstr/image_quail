
## Metrics
### Resolution
- **Definition**: Measures the resolution of the image. Higher resolutions are preferred.
- **Calculation**: `min(height, width) / 1000`
- **Maximum Value**: 10
- **Weight**: 20

### Blurriness
- **Definition**: Assesses the sharpness of the image. Lower variance in the Laplacian filter indicates more blurriness.
- **Calculation**: `min(variance / 100, 10)`
- **Maximum Value**: 10
- **Weight**: 10

### Brightness
- **Definition**: Measures the average brightness of the image. Higher brightness values are preferred.
- **Calculation**: `min(mean_brightness / 255, 10)`
- **Maximum Value**: 10
- **Weight**: 10

### Contrast
- **Definition**: Evaluates the contrast of the image based on the difference between the 98th and 2nd percentiles of pixel intensities.
- **Calculation**: `min(contrast / 100, 10)`
- **Maximum Value**: 10
- **Weight**: 10

## Score Calculation
The total score for each image is calculated using the following formula:
```
Raw Score = (Resolution Score * Weight for Resolution) +
(Blurriness Score * Weight for Blurriness) +
(Brightness Score * Weight for Brightness) +
(Contrast Score * Weight for Contrast)
```

1. Dry Run, scores generated but not compared:
    ```sh
     python main.py --dry_run
    ```
2.  Score comparison, with output file: data/output/differences.csv:
    ```sh
     python main.py
    ```