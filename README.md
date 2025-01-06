# Image deblurring and Object detection

**Dataset preparation**

[GOPRO](https://drive.google.com/file/d/1srx_z-nUfaZVMRrphi6AdOaMKmqyOop8/view?usp=drive_link)

**Installation**

```pip install -r requirements.txt```

**Train**

```python train.py```

**Test**

Pretrained weights can be [found here](https://drive.google.com/file/d/1VfDiGSq30GfcktYg5LqmbVOMQ3tBMoPn/view?usp=sharing)

```python predict.py -i ./test_img -o ./submit -m ./saved_models/fpn_inception.h5``` 

**App**

```python app.py ```

**Credits**

- [DeblurGANv2](https://github.com/VITA-Group/DeblurGANv2)
