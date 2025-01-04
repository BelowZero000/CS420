# Image deblurring and Object detection

**Dataset preparation**

[GOPRO](https://drive.google.com/file/d/1srx_z-nUfaZVMRrphi6AdOaMKmqyOop8/view?usp=drive_link)

**Installation**

```pip install -r requirements.txt```

**Train**

```python train.py```

**Test**

Pretrained weights can be [found here](https://drive.google.com/file/d/1M0zk2udF6GfGgMI84xCcGrUmnyZGsg1T/view?usp=sharing)

```python predict.py -i ./test_img -o ./submit -m ./saved_models/best_fpn.h5``` 

**App**

```python app.py ```

**Colab Notebook**

[Notebook](https://colab.research.google.com/drive/1yHv9dZt_GYQW69RSbShhwR1TChauF9BL?usp=sharing)

**Credits**

- [DeblurGANv2](https://github.com/VITA-Group/DeblurGANv2)
