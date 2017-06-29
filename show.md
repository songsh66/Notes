/usr/bin/python2.7 /home/shuang/workspace/pycharm/trunk/tests/app_test/test_zzsbj_2016.py
welcome bill ocr in python!! 
	your path : /home/shuang/workspace/bill_ocr_work
init logging with file:/home/shuang/workspace/pycharm/trunk/resources/logging/logging.yaml 
0.0691894460242
WARNING: Logging before InitGoogleLogging() is written to STDERR
W0607 09:57:44.717463 16098 _caffe.cpp:135] DEPRECATION WARNING - deprecated use of Python interface
W0607 09:57:44.717478 16098 _caffe.cpp:136] Use this instead (with the named "weights" parameter):
W0607 09:57:44.717480 16098 _caffe.cpp:138] Net('/home/shuang/workspace/pycharm/trunk/resources/caffe/taxidnum/billocrnet_deploy.prototxt', 1, weights='/home/shuang/workspace/pycharm/trunk/resources/caffe/taxidnum/billocr_iter.caffemodel')
I0607 09:57:45.236449 16098 net.cpp:53] Initializing net from parameters: 
name: "DigitNet"
state {
  phase: TEST
  level: 0
}
layer {
  name: "data"
  type: "Input"
  top: "data"
  input_param {
    shape {
      dim: 1
      dim: 1
      dim: 42
      dim: 42
    }
  }
}
layer {
  name: "conv1"
  type: "Convolution"
  bottom: "data"
  top: "conv1"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  convolution_param {
    num_output: 64
    kernel_size: 5
    stride: 1
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "pool1"
  type: "Pooling"
  bottom: "conv1"
  top: "pool1"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  name: "conv2"
  type: "Convolution"
  bottom: "pool1"
  top: "conv2"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  convolution_param {
    num_output: 32
    kernel_size: 5
    stride: 1
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "pool2"
  type: "Pooling"
  bottom: "conv2"
  top: "pool2"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  name: "ip1"
  type: "InnerProduct"
  bottom: "pool2"
  top: "ip1"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  inner_product_param {
    num_output: 800
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "relu1"
  type: "ReLU"
  bottom: "ip1"
  top: "ip1"
}
layer {
  name: "ip2"
  type: "InnerProduct"
  bottom: "ip1"
  top: "ip2"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  inner_product_param {
    num_output: 36
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "prob"
  type: "Softmax"
  bottom: "ip2"
  top: "prob"
}
I0607 09:57:45.236611 16098 layer_factory.hpp:77] Creating layer data
I0607 09:57:45.236639 16098 net.cpp:86] Creating Layer data
I0607 09:57:45.256242 16098 net.cpp:382] data -> data
I0607 09:57:45.342454 16098 net.cpp:124] Setting up data
I0607 09:57:45.342504 16098 net.cpp:131] Top shape: 1 1 42 42 (1764)
I0607 09:57:45.342514 16098 net.cpp:139] Memory required for data: 7056
I0607 09:57:45.342528 16098 layer_factory.hpp:77] Creating layer conv1
I0607 09:57:45.342569 16098 net.cpp:86] Creating Layer conv1
I0607 09:57:45.342579 16098 net.cpp:408] conv1 <- data
I0607 09:57:45.342598 16098 net.cpp:382] conv1 -> conv1
I0607 09:57:47.536201 16098 net.cpp:124] Setting up conv1
I0607 09:57:47.536221 16098 net.cpp:131] Top shape: 1 64 38 38 (92416)
I0607 09:57:47.536224 16098 net.cpp:139] Memory required for data: 376720
I0607 09:57:47.536238 16098 layer_factory.hpp:77] Creating layer pool1
I0607 09:57:47.536249 16098 net.cpp:86] Creating Layer pool1
I0607 09:57:47.536252 16098 net.cpp:408] pool1 <- conv1
I0607 09:57:47.536257 16098 net.cpp:382] pool1 -> pool1
I0607 09:57:47.536270 16098 net.cpp:124] Setting up pool1
I0607 09:57:47.536274 16098 net.cpp:131] Top shape: 1 64 19 19 (23104)
I0607 09:57:47.536276 16098 net.cpp:139] Memory required for data: 469136
I0607 09:57:47.536279 16098 layer_factory.hpp:77] Creating layer conv2
I0607 09:57:47.536289 16098 net.cpp:86] Creating Layer conv2
I0607 09:57:47.536291 16098 net.cpp:408] conv2 <- pool1
I0607 09:57:47.536295 16098 net.cpp:382] conv2 -> conv2
I0607 09:57:47.539446 16098 net.cpp:124] Setting up conv2
I0607 09:57:47.539459 16098 net.cpp:131] Top shape: 1 32 15 15 (7200)
I0607 09:57:47.539463 16098 net.cpp:139] Memory required for data: 497936
I0607 09:57:47.539474 16098 layer_factory.hpp:77] Creating layer pool2
I0607 09:57:47.539481 16098 net.cpp:86] Creating Layer pool2
I0607 09:57:47.539484 16098 net.cpp:408] pool2 <- conv2
I0607 09:57:47.539489 16098 net.cpp:382] pool2 -> pool2
I0607 09:57:47.539501 16098 net.cpp:124] Setting up pool2
I0607 09:57:47.539506 16098 net.cpp:131] Top shape: 1 32 8 8 (2048)
I0607 09:57:47.539510 16098 net.cpp:139] Memory required for data: 506128
I0607 09:57:47.539511 16098 layer_factory.hpp:77] Creating layer ip1
I0607 09:57:47.539517 16098 net.cpp:86] Creating Layer ip1
I0607 09:57:47.539520 16098 net.cpp:408] ip1 <- pool2
I0607 09:57:47.539526 16098 net.cpp:382] ip1 -> ip1
I0607 09:57:47.549379 16098 net.cpp:124] Setting up ip1
I0607 09:57:47.549392 16098 net.cpp:131] Top shape: 1 800 (800)
I0607 09:57:47.549394 16098 net.cpp:139] Memory required for data: 509328
I0607 09:57:47.549403 16098 layer_factory.hpp:77] Creating layer relu1
I0607 09:57:47.549410 16098 net.cpp:86] Creating Layer relu1
I0607 09:57:47.549412 16098 net.cpp:408] relu1 <- ip1
I0607 09:57:47.549417 16098 net.cpp:369] relu1 -> ip1 (in-place)
I0607 09:57:47.549607 16098 net.cpp:124] Setting up relu1
I0607 09:57:47.549613 16098 net.cpp:131] Top shape: 1 800 (800)
I0607 09:57:47.549614 16098 net.cpp:139] Memory required for data: 512528
I0607 09:57:47.549618 16098 layer_factory.hpp:77] Creating layer ip2
I0607 09:57:47.549623 16098 net.cpp:86] Creating Layer ip2
I0607 09:57:47.549625 16098 net.cpp:408] ip2 <- ip1
I0607 09:57:47.549629 16098 net.cpp:382] ip2 -> ip2
I0607 09:57:47.549800 16098 net.cpp:124] Setting up ip2
I0607 09:57:47.549803 16098 net.cpp:131] Top shape: 1 36 (36)
I0607 09:57:47.549805 16098 net.cpp:139] Memory required for data: 512672
I0607 09:57:47.549809 16098 layer_factory.hpp:77] Creating layer prob
I0607 09:57:47.549814 16098 net.cpp:86] Creating Layer prob
I0607 09:57:47.549816 16098 net.cpp:408] prob <- ip2
I0607 09:57:47.549819 16098 net.cpp:382] prob -> prob
I0607 09:57:47.550386 16098 net.cpp:124] Setting up prob
I0607 09:57:47.550393 16098 net.cpp:131] Top shape: 1 36 (36)
I0607 09:57:47.550396 16098 net.cpp:139] Memory required for data: 512816
I0607 09:57:47.550398 16098 net.cpp:202] prob does not need backward computation.
I0607 09:57:47.550400 16098 net.cpp:202] ip2 does not need backward computation.
I0607 09:57:47.550402 16098 net.cpp:202] relu1 does not need backward computation.
I0607 09:57:47.550405 16098 net.cpp:202] ip1 does not need backward computation.
I0607 09:57:47.550407 16098 net.cpp:202] pool2 does not need backward computation.
I0607 09:57:47.550410 16098 net.cpp:202] conv2 does not need backward computation.
I0607 09:57:47.550411 16098 net.cpp:202] pool1 does not need backward computation.
I0607 09:57:47.550413 16098 net.cpp:202] conv1 does not need backward computation.
I0607 09:57:47.550415 16098 net.cpp:202] data does not need backward computation.
I0607 09:57:47.550416 16098 net.cpp:244] This network produces output prob
I0607 09:57:47.550423 16098 net.cpp:257] Network initialization done.
I0607 09:57:47.603618 16098 net.cpp:746] Ignoring source layer digits
I0607 09:57:47.607017 16098 net.cpp:746] Ignoring source layer loss
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/saler_no_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
W0607 09:57:47.741439 16098 _caffe.cpp:135] DEPRECATION WARNING - deprecated use of Python interface
W0607 09:57:47.741466 16098 _caffe.cpp:136] Use this instead (with the named "weights" parameter):
W0607 09:57:47.741470 16098 _caffe.cpp:138] Net('/home/shuang/workspace/pycharm/trunk/resources/caffe/cnchar/billocrnet_deploy.prototxt', 1, weights='/home/shuang/workspace/pycharm/trunk/resources/caffe/cnchar/billocr_iter.caffemodel')
I0607 09:57:47.741732 16098 net.cpp:53] Initializing net from parameters: 
name: "CnCharNet"
state {
  phase: TEST
  level: 0
}
layer {
  name: "data"
  type: "Input"
  top: "data"
  input_param {
    shape {
      dim: 1
      dim: 1
      dim: 42
      dim: 42
    }
  }
}
layer {
  name: "conv1"
  type: "Convolution"
  bottom: "data"
  top: "conv1"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  convolution_param {
    num_output: 32
    kernel_size: 3
    stride: 1
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "pool1"
  type: "Pooling"
  bottom: "conv1"
  top: "pool1"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  name: "conv2"
  type: "Convolution"
  bottom: "pool1"
  top: "conv2"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  convolution_param {
    num_output: 64
    kernel_size: 3
    stride: 1
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "pool2"
  type: "Pooling"
  bottom: "conv2"
  top: "pool2"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  name: "conv3"
  type: "Convolution"
  bottom: "pool2"
  top: "conv3"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  convolution_param {
    num_output: 128
    kernel_size: 3
    stride: 1
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "pool3"
  type: "Pooling"
  bottom: "conv3"
  top: "pool3"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  name: "ip1"
  type: "InnerProduct"
  bottom: "pool3"
  top: "ip1"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  inner_product_param {
    num_output: 2000
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "relu1"
  type: "ReLU"
  bottom: "ip1"
  top: "ip1"
}
layer {
  name: "ip2"
  type: "InnerProduct"
  bottom: "ip1"
  top: "ip2"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  inner_product_param {
    num_output: 3853
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "prob"
  type: "Softmax"
  bottom: "ip2"
  top: "prob"
}
I0607 09:57:47.741776 16098 layer_factory.hpp:77] Creating layer data
I0607 09:57:47.741786 16098 net.cpp:86] Creating Layer data
I0607 09:57:47.741791 16098 net.cpp:382] data -> data
I0607 09:57:47.741808 16098 net.cpp:124] Setting up data
I0607 09:57:47.741814 16098 net.cpp:131] Top shape: 1 1 42 42 (1764)
I0607 09:57:47.741817 16098 net.cpp:139] Memory required for data: 7056
I0607 09:57:47.741822 16098 layer_factory.hpp:77] Creating layer conv1
I0607 09:57:47.741832 16098 net.cpp:86] Creating Layer conv1
I0607 09:57:47.741834 16098 net.cpp:408] conv1 <- data
I0607 09:57:47.741840 16098 net.cpp:382] conv1 -> conv1
I0607 09:57:47.743247 16098 net.cpp:124] Setting up conv1
I0607 09:57:47.743265 16098 net.cpp:131] Top shape: 1 32 40 40 (51200)
I0607 09:57:47.743269 16098 net.cpp:139] Memory required for data: 211856
I0607 09:57:47.743283 16098 layer_factory.hpp:77] Creating layer pool1
I0607 09:57:47.743294 16098 net.cpp:86] Creating Layer pool1
I0607 09:57:47.743296 16098 net.cpp:408] pool1 <- conv1
I0607 09:57:47.743301 16098 net.cpp:382] pool1 -> pool1
I0607 09:57:47.743312 16098 net.cpp:124] Setting up pool1
I0607 09:57:47.743317 16098 net.cpp:131] Top shape: 1 32 20 20 (12800)
I0607 09:57:47.743320 16098 net.cpp:139] Memory required for data: 263056
I0607 09:57:47.743322 16098 layer_factory.hpp:77] Creating layer conv2
I0607 09:57:47.743333 16098 net.cpp:86] Creating Layer conv2
I0607 09:57:47.743337 16098 net.cpp:408] conv2 <- pool1
I0607 09:57:47.743342 16098 net.cpp:382] conv2 -> conv2
I0607 09:57:47.744115 16098 net.cpp:124] Setting up conv2
I0607 09:57:47.744127 16098 net.cpp:131] Top shape: 1 64 18 18 (20736)
I0607 09:57:47.744130 16098 net.cpp:139] Memory required for data: 346000
I0607 09:57:47.744138 16098 layer_factory.hpp:77] Creating layer pool2
I0607 09:57:47.744145 16098 net.cpp:86] Creating Layer pool2
I0607 09:57:47.744148 16098 net.cpp:408] pool2 <- conv2
I0607 09:57:47.744154 16098 net.cpp:382] pool2 -> pool2
I0607 09:57:47.744163 16098 net.cpp:124] Setting up pool2
I0607 09:57:47.744168 16098 net.cpp:131] Top shape: 1 64 9 9 (5184)
I0607 09:57:47.744170 16098 net.cpp:139] Memory required for data: 366736
I0607 09:57:47.744174 16098 layer_factory.hpp:77] Creating layer conv3
I0607 09:57:47.744182 16098 net.cpp:86] Creating Layer conv3
I0607 09:57:47.744185 16098 net.cpp:408] conv3 <- pool2
I0607 09:57:47.744191 16098 net.cpp:382] conv3 -> conv3
I0607 09:57:47.746521 16098 net.cpp:124] Setting up conv3
I0607 09:57:47.746539 16098 net.cpp:131] Top shape: 1 128 7 7 (6272)
I0607 09:57:47.746542 16098 net.cpp:139] Memory required for data: 391824
I0607 09:57:47.746552 16098 layer_factory.hpp:77] Creating layer pool3
I0607 09:57:47.746562 16098 net.cpp:86] Creating Layer pool3
I0607 09:57:47.746564 16098 net.cpp:408] pool3 <- conv3
I0607 09:57:47.746570 16098 net.cpp:382] pool3 -> pool3
I0607 09:57:47.746582 16098 net.cpp:124] Setting up pool3
I0607 09:57:47.746585 16098 net.cpp:131] Top shape: 1 128 4 4 (2048)
I0607 09:57:47.746588 16098 net.cpp:139] Memory required for data: 400016
I0607 09:57:47.746590 16098 layer_factory.hpp:77] Creating layer ip1
I0607 09:57:47.746598 16098 net.cpp:86] Creating Layer ip1
I0607 09:57:47.746600 16098 net.cpp:408] ip1 <- pool3
I0607 09:57:47.746605 16098 net.cpp:382] ip1 -> ip1
I0607 09:57:47.776166 16098 net.cpp:124] Setting up ip1
I0607 09:57:47.776183 16098 net.cpp:131] Top shape: 1 2000 (2000)
I0607 09:57:47.776186 16098 net.cpp:139] Memory required for data: 408016
I0607 09:57:47.776192 16098 layer_factory.hpp:77] Creating layer relu1
I0607 09:57:47.776203 16098 net.cpp:86] Creating Layer relu1
I0607 09:57:47.776206 16098 net.cpp:408] relu1 <- ip1
I0607 09:57:47.776211 16098 net.cpp:369] relu1 -> ip1 (in-place)
I0607 09:57:47.776903 16098 net.cpp:124] Setting up relu1
I0607 09:57:47.776913 16098 net.cpp:131] Top shape: 1 2000 (2000)
I0607 09:57:47.776916 16098 net.cpp:139] Memory required for data: 416016
I0607 09:57:47.776919 16098 layer_factory.hpp:77] Creating layer ip2
I0607 09:57:47.776928 16098 net.cpp:86] Creating Layer ip2
I0607 09:57:47.776932 16098 net.cpp:408] ip2 <- ip1
I0607 09:57:47.776935 16098 net.cpp:382] ip2 -> ip2
I0607 09:57:47.825552 16098 net.cpp:124] Setting up ip2
I0607 09:57:47.825569 16098 net.cpp:131] Top shape: 1 3853 (3853)
I0607 09:57:47.825572 16098 net.cpp:139] Memory required for data: 431428
I0607 09:57:47.825582 16098 layer_factory.hpp:77] Creating layer prob
I0607 09:57:47.825590 16098 net.cpp:86] Creating Layer prob
I0607 09:57:47.825593 16098 net.cpp:408] prob <- ip2
I0607 09:57:47.825598 16098 net.cpp:382] prob -> prob
I0607 09:57:47.825803 16098 net.cpp:124] Setting up prob
I0607 09:57:47.825809 16098 net.cpp:131] Top shape: 1 3853 (3853)
I0607 09:57:47.825811 16098 net.cpp:139] Memory required for data: 446840
I0607 09:57:47.825814 16098 net.cpp:202] prob does not need backward computation.
I0607 09:57:47.825816 16098 net.cpp:202] ip2 does not need backward computation.
I0607 09:57:47.825819 16098 net.cpp:202] relu1 does not need backward computation.
I0607 09:57:47.825821 16098 net.cpp:202] ip1 does not need backward computation.
I0607 09:57:47.825824 16098 net.cpp:202] pool3 does not need backward computation.
I0607 09:57:47.825826 16098 net.cpp:202] conv3 does not need backward computation.
I0607 09:57:47.825829 16098 net.cpp:202] pool2 does not need backward computation.
I0607 09:57:47.825830 16098 net.cpp:202] conv2 does not need backward computation.
I0607 09:57:47.825834 16098 net.cpp:202] pool1 does not need backward computation.
I0607 09:57:47.825835 16098 net.cpp:202] conv1 does not need backward computation.
I0607 09:57:47.825837 16098 net.cpp:202] data does not need backward computation.
I0607 09:57:47.825839 16098 net.cpp:244] This network produces output prob
I0607 09:57:47.825852 16098 net.cpp:257] Network initialization done.
I0607 09:57:48.096046 16098 net.cpp:746] Ignoring source layer cnchars
I0607 09:57:48.121103 16098 net.cpp:746] Ignoring source layer loss
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/buyer_name_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
W0607 09:57:48.238108 16098 _caffe.cpp:135] DEPRECATION WARNING - deprecated use of Python interface
W0607 09:57:48.238126 16098 _caffe.cpp:136] Use this instead (with the named "weights" parameter):
W0607 09:57:48.238128 16098 _caffe.cpp:138] Net('/home/shuang/workspace/pycharm/trunk/resources/caffe/amountsmall/billocrnet_deploy.prototxt', 1, weights='/home/shuang/workspace/pycharm/trunk/resources/caffe/amountsmall/billocr_iter.caffemodel')
I0607 09:57:48.238371 16098 net.cpp:53] Initializing net from parameters: 
name: "DigitNet"
state {
  phase: TEST
  level: 0
}
layer {
  name: "data"
  type: "Input"
  top: "data"
  input_param {
    shape {
      dim: 1
      dim: 1
      dim: 42
      dim: 42
    }
  }
}
layer {
  name: "conv1"
  type: "Convolution"
  bottom: "data"
  top: "conv1"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  convolution_param {
    num_output: 64
    kernel_size: 5
    stride: 1
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "pool1"
  type: "Pooling"
  bottom: "conv1"
  top: "pool1"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  name: "conv2"
  type: "Convolution"
  bottom: "pool1"
  top: "conv2"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  convolution_param {
    num_output: 32
    kernel_size: 5
    stride: 1
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "pool2"
  type: "Pooling"
  bottom: "conv2"
  top: "pool2"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  name: "ip1"
  type: "InnerProduct"
  bottom: "pool2"
  top: "ip1"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  inner_product_param {
    num_output: 800
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "relu1"
  type: "ReLU"
  bottom: "ip1"
  top: "ip1"
}
layer {
  name: "ip2"
  type: "InnerProduct"
  bottom: "ip1"
  top: "ip2"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  inner_product_param {
    num_output: 13
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "prob"
  type: "Softmax"
  bottom: "ip2"
  top: "prob"
}
I0607 09:57:48.238411 16098 layer_factory.hpp:77] Creating layer data
I0607 09:57:48.238420 16098 net.cpp:86] Creating Layer data
I0607 09:57:48.238425 16098 net.cpp:382] data -> data
I0607 09:57:48.238443 16098 net.cpp:124] Setting up data
I0607 09:57:48.238451 16098 net.cpp:131] Top shape: 1 1 42 42 (1764)
I0607 09:57:48.238453 16098 net.cpp:139] Memory required for data: 7056
I0607 09:57:48.238456 16098 layer_factory.hpp:77] Creating layer conv1
I0607 09:57:48.238467 16098 net.cpp:86] Creating Layer conv1
I0607 09:57:48.238471 16098 net.cpp:408] conv1 <- data
I0607 09:57:48.238477 16098 net.cpp:382] conv1 -> conv1
I0607 09:57:48.239848 16098 net.cpp:124] Setting up conv1
I0607 09:57:48.239861 16098 net.cpp:131] Top shape: 1 64 38 38 (92416)
I0607 09:57:48.239864 16098 net.cpp:139] Memory required for data: 376720
I0607 09:57:48.239874 16098 layer_factory.hpp:77] Creating layer pool1
I0607 09:57:48.239881 16098 net.cpp:86] Creating Layer pool1
I0607 09:57:48.239886 16098 net.cpp:408] pool1 <- conv1
I0607 09:57:48.239890 16098 net.cpp:382] pool1 -> pool1
I0607 09:57:48.239900 16098 net.cpp:124] Setting up pool1
I0607 09:57:48.239905 16098 net.cpp:131] Top shape: 1 64 19 19 (23104)
I0607 09:57:48.239908 16098 net.cpp:139] Memory required for data: 469136
I0607 09:57:48.239912 16098 layer_factory.hpp:77] Creating layer conv2
I0607 09:57:48.239919 16098 net.cpp:86] Creating Layer conv2
I0607 09:57:48.239923 16098 net.cpp:408] conv2 <- pool1
I0607 09:57:48.239929 16098 net.cpp:382] conv2 -> conv2
I0607 09:57:48.241506 16098 net.cpp:124] Setting up conv2
I0607 09:57:48.241515 16098 net.cpp:131] Top shape: 1 32 15 15 (7200)
I0607 09:57:48.241519 16098 net.cpp:139] Memory required for data: 497936
I0607 09:57:48.241528 16098 layer_factory.hpp:77] Creating layer pool2
I0607 09:57:48.241535 16098 net.cpp:86] Creating Layer pool2
I0607 09:57:48.241539 16098 net.cpp:408] pool2 <- conv2
I0607 09:57:48.241544 16098 net.cpp:382] pool2 -> pool2
I0607 09:57:48.241554 16098 net.cpp:124] Setting up pool2
I0607 09:57:48.241559 16098 net.cpp:131] Top shape: 1 32 8 8 (2048)
I0607 09:57:48.241561 16098 net.cpp:139] Memory required for data: 506128
I0607 09:57:48.241564 16098 layer_factory.hpp:77] Creating layer ip1
I0607 09:57:48.241572 16098 net.cpp:86] Creating Layer ip1
I0607 09:57:48.241575 16098 net.cpp:408] ip1 <- pool2
I0607 09:57:48.241580 16098 net.cpp:382] ip1 -> ip1
I0607 09:57:48.254942 16098 net.cpp:124] Setting up ip1
I0607 09:57:48.254964 16098 net.cpp:131] Top shape: 1 800 (800)
I0607 09:57:48.254967 16098 net.cpp:139] Memory required for data: 509328
I0607 09:57:48.254978 16098 layer_factory.hpp:77] Creating layer relu1
I0607 09:57:48.254987 16098 net.cpp:86] Creating Layer relu1
I0607 09:57:48.254992 16098 net.cpp:408] relu1 <- ip1
I0607 09:57:48.254997 16098 net.cpp:369] relu1 -> ip1 (in-place)
I0607 09:57:48.255241 16098 net.cpp:124] Setting up relu1
I0607 09:57:48.255249 16098 net.cpp:131] Top shape: 1 800 (800)
I0607 09:57:48.255252 16098 net.cpp:139] Memory required for data: 512528
I0607 09:57:48.255255 16098 layer_factory.hpp:77] Creating layer ip2
I0607 09:57:48.255264 16098 net.cpp:86] Creating Layer ip2
I0607 09:57:48.255266 16098 net.cpp:408] ip2 <- ip1
I0607 09:57:48.255271 16098 net.cpp:382] ip2 -> ip2
I0607 09:57:48.255383 16098 net.cpp:124] Setting up ip2
I0607 09:57:48.255388 16098 net.cpp:131] Top shape: 1 13 (13)
I0607 09:57:48.255390 16098 net.cpp:139] Memory required for data: 512580
I0607 09:57:48.255395 16098 layer_factory.hpp:77] Creating layer prob
I0607 09:57:48.255403 16098 net.cpp:86] Creating Layer prob
I0607 09:57:48.255405 16098 net.cpp:408] prob <- ip2
I0607 09:57:48.255410 16098 net.cpp:382] prob -> prob
I0607 09:57:48.255599 16098 net.cpp:124] Setting up prob
I0607 09:57:48.255604 16098 net.cpp:131] Top shape: 1 13 (13)
I0607 09:57:48.255607 16098 net.cpp:139] Memory required for data: 512632
I0607 09:57:48.255611 16098 net.cpp:202] prob does not need backward computation.
I0607 09:57:48.255614 16098 net.cpp:202] ip2 does not need backward computation.
I0607 09:57:48.255617 16098 net.cpp:202] relu1 does not need backward computation.
I0607 09:57:48.255620 16098 net.cpp:202] ip1 does not need backward computation.
I0607 09:57:48.255623 16098 net.cpp:202] pool2 does not need backward computation.
I0607 09:57:48.255627 16098 net.cpp:202] conv2 does not need backward computation.
I0607 09:57:48.255630 16098 net.cpp:202] pool1 does not need backward computation.
I0607 09:57:48.255633 16098 net.cpp:202] conv1 does not need backward computation.
I0607 09:57:48.255636 16098 net.cpp:202] data does not need backward computation.
I0607 09:57:48.255640 16098 net.cpp:244] This network produces output prob
I0607 09:57:48.255647 16098 net.cpp:257] Network initialization done.
I0607 09:57:48.304358 16098 net.cpp:746] Ignoring source layer digits
I0607 09:57:48.305871 16098 net.cpp:746] Ignoring source layer loss
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/item_price_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/item_money_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/saler_name_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/saler_address_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/saler_address_1.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/buyer_address_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/buyer_bankaccount_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/money_small_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/money_small_1.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/money_small_2.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
W0607 09:57:49.250388 16098 _caffe.cpp:135] DEPRECATION WARNING - deprecated use of Python interface
W0607 09:57:49.250404 16098 _caffe.cpp:136] Use this instead (with the named "weights" parameter):
W0607 09:57:49.250406 16098 _caffe.cpp:138] Net('/home/shuang/workspace/pycharm/trunk/resources/caffe/date/billocrnet_deploy.prototxt', 1, weights='/home/shuang/workspace/pycharm/trunk/resources/caffe/date/billocr_iter.caffemodel')
I0607 09:57:49.250591 16098 net.cpp:53] Initializing net from parameters: 
name: "DigitNet"
state {
  phase: TEST
  level: 0
}
layer {
  name: "data"
  type: "Input"
  top: "data"
  input_param {
    shape {
      dim: 1
      dim: 1
      dim: 42
      dim: 42
    }
  }
}
layer {
  name: "conv1"
  type: "Convolution"
  bottom: "data"
  top: "conv1"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  convolution_param {
    num_output: 64
    kernel_size: 5
    stride: 1
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "pool1"
  type: "Pooling"
  bottom: "conv1"
  top: "pool1"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  name: "conv2"
  type: "Convolution"
  bottom: "pool1"
  top: "conv2"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  convolution_param {
    num_output: 32
    kernel_size: 5
    stride: 1
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "pool2"
  type: "Pooling"
  bottom: "conv2"
  top: "pool2"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  name: "ip1"
  type: "InnerProduct"
  bottom: "pool2"
  top: "ip1"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  inner_product_param {
    num_output: 800
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "relu1"
  type: "ReLU"
  bottom: "ip1"
  top: "ip1"
}
layer {
  name: "ip2"
  type: "InnerProduct"
  bottom: "ip1"
  top: "ip2"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  inner_product_param {
    num_output: 16
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "prob"
  type: "Softmax"
  bottom: "ip2"
  top: "prob"
}
I0607 09:57:49.250619 16098 layer_factory.hpp:77] Creating layer data
I0607 09:57:49.250627 16098 net.cpp:86] Creating Layer data
I0607 09:57:49.250629 16098 net.cpp:382] data -> data
I0607 09:57:49.250645 16098 net.cpp:124] Setting up data
I0607 09:57:49.250650 16098 net.cpp:131] Top shape: 1 1 42 42 (1764)
I0607 09:57:49.250653 16098 net.cpp:139] Memory required for data: 7056
I0607 09:57:49.250654 16098 layer_factory.hpp:77] Creating layer conv1
I0607 09:57:49.250661 16098 net.cpp:86] Creating Layer conv1
I0607 09:57:49.250664 16098 net.cpp:408] conv1 <- data
I0607 09:57:49.250668 16098 net.cpp:382] conv1 -> conv1
I0607 09:57:49.251723 16098 net.cpp:124] Setting up conv1
I0607 09:57:49.251730 16098 net.cpp:131] Top shape: 1 64 38 38 (92416)
I0607 09:57:49.251734 16098 net.cpp:139] Memory required for data: 376720
I0607 09:57:49.251740 16098 layer_factory.hpp:77] Creating layer pool1
I0607 09:57:49.251745 16098 net.cpp:86] Creating Layer pool1
I0607 09:57:49.251747 16098 net.cpp:408] pool1 <- conv1
I0607 09:57:49.251751 16098 net.cpp:382] pool1 -> pool1
I0607 09:57:49.251758 16098 net.cpp:124] Setting up pool1
I0607 09:57:49.251761 16098 net.cpp:131] Top shape: 1 64 19 19 (23104)
I0607 09:57:49.251763 16098 net.cpp:139] Memory required for data: 469136
I0607 09:57:49.251765 16098 layer_factory.hpp:77] Creating layer conv2
I0607 09:57:49.251770 16098 net.cpp:86] Creating Layer conv2
I0607 09:57:49.251772 16098 net.cpp:408] conv2 <- pool1
I0607 09:57:49.251775 16098 net.cpp:382] conv2 -> conv2
I0607 09:57:49.253654 16098 net.cpp:124] Setting up conv2
I0607 09:57:49.253669 16098 net.cpp:131] Top shape: 1 32 15 15 (7200)
I0607 09:57:49.253672 16098 net.cpp:139] Memory required for data: 497936
I0607 09:57:49.253684 16098 layer_factory.hpp:77] Creating layer pool2
I0607 09:57:49.253695 16098 net.cpp:86] Creating Layer pool2
I0607 09:57:49.253700 16098 net.cpp:408] pool2 <- conv2
I0607 09:57:49.253705 16098 net.cpp:382] pool2 -> pool2
I0607 09:57:49.253718 16098 net.cpp:124] Setting up pool2
I0607 09:57:49.253724 16098 net.cpp:131] Top shape: 1 32 8 8 (2048)
I0607 09:57:49.253727 16098 net.cpp:139] Memory required for data: 506128
I0607 09:57:49.253731 16098 layer_factory.hpp:77] Creating layer ip1
I0607 09:57:49.253738 16098 net.cpp:86] Creating Layer ip1
I0607 09:57:49.253742 16098 net.cpp:408] ip1 <- pool2
I0607 09:57:49.253747 16098 net.cpp:382] ip1 -> ip1
I0607 09:57:49.266788 16098 net.cpp:124] Setting up ip1
I0607 09:57:49.266811 16098 net.cpp:131] Top shape: 1 800 (800)
I0607 09:57:49.266814 16098 net.cpp:139] Memory required for data: 509328
I0607 09:57:49.266826 16098 layer_factory.hpp:77] Creating layer relu1
I0607 09:57:49.266835 16098 net.cpp:86] Creating Layer relu1
I0607 09:57:49.266837 16098 net.cpp:408] relu1 <- ip1
I0607 09:57:49.266844 16098 net.cpp:369] relu1 -> ip1 (in-place)
I0607 09:57:49.267066 16098 net.cpp:124] Setting up relu1
I0607 09:57:49.267072 16098 net.cpp:131] Top shape: 1 800 (800)
I0607 09:57:49.267074 16098 net.cpp:139] Memory required for data: 512528
I0607 09:57:49.267076 16098 layer_factory.hpp:77] Creating layer ip2
I0607 09:57:49.267083 16098 net.cpp:86] Creating Layer ip2
I0607 09:57:49.267086 16098 net.cpp:408] ip2 <- ip1
I0607 09:57:49.267091 16098 net.cpp:382] ip2 -> ip2
I0607 09:57:49.267195 16098 net.cpp:124] Setting up ip2
I0607 09:57:49.267199 16098 net.cpp:131] Top shape: 1 16 (16)
I0607 09:57:49.267200 16098 net.cpp:139] Memory required for data: 512592
I0607 09:57:49.267204 16098 layer_factory.hpp:77] Creating layer prob
I0607 09:57:49.267211 16098 net.cpp:86] Creating Layer prob
I0607 09:57:49.267215 16098 net.cpp:408] prob <- ip2
I0607 09:57:49.267217 16098 net.cpp:382] prob -> prob
I0607 09:57:49.267843 16098 net.cpp:124] Setting up prob
I0607 09:57:49.267851 16098 net.cpp:131] Top shape: 1 16 (16)
I0607 09:57:49.267853 16098 net.cpp:139] Memory required for data: 512656
I0607 09:57:49.267856 16098 net.cpp:202] prob does not need backward computation.
I0607 09:57:49.267859 16098 net.cpp:202] ip2 does not need backward computation.
I0607 09:57:49.267861 16098 net.cpp:202] relu1 does not need backward computation.
I0607 09:57:49.267863 16098 net.cpp:202] ip1 does not need backward computation.
I0607 09:57:49.267866 16098 net.cpp:202] pool2 does not need backward computation.
I0607 09:57:49.267868 16098 net.cpp:202] conv2 does not need backward computation.
I0607 09:57:49.267871 16098 net.cpp:202] pool1 does not need backward computation.
I0607 09:57:49.267874 16098 net.cpp:202] conv1 does not need backward computation.
I0607 09:57:49.267875 16098 net.cpp:202] data does not need backward computation.
I0607 09:57:49.267877 16098 net.cpp:244] This network produces output prob
I0607 09:57:49.267885 16098 net.cpp:257] Network initialization done.
I0607 09:57:49.310636 16098 net.cpp:746] Ignoring source layer digits
I0607 09:57:49.311821 16098 net.cpp:746] Ignoring source layer loss
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/date_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
W0607 09:57:49.365080 16098 _caffe.cpp:135] DEPRECATION WARNING - deprecated use of Python interface
W0607 09:57:49.365097 16098 _caffe.cpp:136] Use this instead (with the named "weights" parameter):
W0607 09:57:49.365099 16098 _caffe.cpp:138] Net('/home/shuang/workspace/pycharm/trunk/resources/caffe/password_area/billocrnet_deploy.prototxt', 1, weights='/home/shuang/workspace/pycharm/trunk/resources/caffe/password_area/billocr_iter.caffemodel')
I0607 09:57:49.365291 16098 net.cpp:53] Initializing net from parameters: 
name: "DigitNet"
state {
  phase: TEST
  level: 0
}
layer {
  name: "data"
  type: "Input"
  top: "data"
  input_param {
    shape {
      dim: 1
      dim: 1
      dim: 42
      dim: 42
    }
  }
}
layer {
  name: "conv1"
  type: "Convolution"
  bottom: "data"
  top: "conv1"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  convolution_param {
    num_output: 64
    kernel_size: 5
    stride: 1
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "pool1"
  type: "Pooling"
  bottom: "conv1"
  top: "pool1"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  name: "conv2"
  type: "Convolution"
  bottom: "pool1"
  top: "conv2"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  convolution_param {
    num_output: 32
    kernel_size: 5
    stride: 1
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "pool2"
  type: "Pooling"
  bottom: "conv2"
  top: "pool2"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  name: "ip1"
  type: "InnerProduct"
  bottom: "pool2"
  top: "ip1"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  inner_product_param {
    num_output: 800
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "relu1"
  type: "ReLU"
  bottom: "ip1"
  top: "ip1"
}
layer {
  name: "ip2"
  type: "InnerProduct"
  bottom: "ip1"
  top: "ip2"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  inner_product_param {
    num_output: 16
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "prob"
  type: "Softmax"
  bottom: "ip2"
  top: "prob"
}
I0607 09:57:49.365325 16098 layer_factory.hpp:77] Creating layer data
I0607 09:57:49.365332 16098 net.cpp:86] Creating Layer data
I0607 09:57:49.365336 16098 net.cpp:382] data -> data
I0607 09:57:49.365353 16098 net.cpp:124] Setting up data
I0607 09:57:49.365360 16098 net.cpp:131] Top shape: 1 1 42 42 (1764)
I0607 09:57:49.365361 16098 net.cpp:139] Memory required for data: 7056
I0607 09:57:49.365365 16098 layer_factory.hpp:77] Creating layer conv1
I0607 09:57:49.365372 16098 net.cpp:86] Creating Layer conv1
I0607 09:57:49.365375 16098 net.cpp:408] conv1 <- data
I0607 09:57:49.365381 16098 net.cpp:382] conv1 -> conv1
I0607 09:57:49.366030 16098 net.cpp:124] Setting up conv1
I0607 09:57:49.366039 16098 net.cpp:131] Top shape: 1 64 38 38 (92416)
I0607 09:57:49.366040 16098 net.cpp:139] Memory required for data: 376720
I0607 09:57:49.366050 16098 layer_factory.hpp:77] Creating layer pool1
I0607 09:57:49.366055 16098 net.cpp:86] Creating Layer pool1
I0607 09:57:49.366057 16098 net.cpp:408] pool1 <- conv1
I0607 09:57:49.366061 16098 net.cpp:382] pool1 -> pool1
I0607 09:57:49.366068 16098 net.cpp:124] Setting up pool1
I0607 09:57:49.366072 16098 net.cpp:131] Top shape: 1 64 19 19 (23104)
I0607 09:57:49.366075 16098 net.cpp:139] Memory required for data: 469136
I0607 09:57:49.366076 16098 layer_factory.hpp:77] Creating layer conv2
I0607 09:57:49.366082 16098 net.cpp:86] Creating Layer conv2
I0607 09:57:49.366086 16098 net.cpp:408] conv2 <- pool1
I0607 09:57:49.366089 16098 net.cpp:382] conv2 -> conv2
I0607 09:57:49.367396 16098 net.cpp:124] Setting up conv2
I0607 09:57:49.367405 16098 net.cpp:131] Top shape: 1 32 15 15 (7200)
I0607 09:57:49.367408 16098 net.cpp:139] Memory required for data: 497936
I0607 09:57:49.367415 16098 layer_factory.hpp:77] Creating layer pool2
I0607 09:57:49.367420 16098 net.cpp:86] Creating Layer pool2
I0607 09:57:49.367424 16098 net.cpp:408] pool2 <- conv2
I0607 09:57:49.367427 16098 net.cpp:382] pool2 -> pool2
I0607 09:57:49.367435 16098 net.cpp:124] Setting up pool2
I0607 09:57:49.367439 16098 net.cpp:131] Top shape: 1 32 8 8 (2048)
I0607 09:57:49.367441 16098 net.cpp:139] Memory required for data: 506128
I0607 09:57:49.367444 16098 layer_factory.hpp:77] Creating layer ip1
I0607 09:57:49.367449 16098 net.cpp:86] Creating Layer ip1
I0607 09:57:49.367450 16098 net.cpp:408] ip1 <- pool2
I0607 09:57:49.367455 16098 net.cpp:382] ip1 -> ip1
I0607 09:57:49.378047 16098 net.cpp:124] Setting up ip1
I0607 09:57:49.378059 16098 net.cpp:131] Top shape: 1 800 (800)
I0607 09:57:49.378062 16098 net.cpp:139] Memory required for data: 509328
I0607 09:57:49.378069 16098 layer_factory.hpp:77] Creating layer relu1
I0607 09:57:49.378077 16098 net.cpp:86] Creating Layer relu1
I0607 09:57:49.378078 16098 net.cpp:408] relu1 <- ip1
I0607 09:57:49.378083 16098 net.cpp:369] relu1 -> ip1 (in-place)
I0607 09:57:49.378721 16098 net.cpp:124] Setting up relu1
I0607 09:57:49.378729 16098 net.cpp:131] Top shape: 1 800 (800)
I0607 09:57:49.378731 16098 net.cpp:139] Memory required for data: 512528
I0607 09:57:49.378734 16098 layer_factory.hpp:77] Creating layer ip2
I0607 09:57:49.378741 16098 net.cpp:86] Creating Layer ip2
I0607 09:57:49.378744 16098 net.cpp:408] ip2 <- ip1
I0607 09:57:49.378748 16098 net.cpp:382] ip2 -> ip2
I0607 09:57:49.378849 16098 net.cpp:124] Setting up ip2
I0607 09:57:49.378854 16098 net.cpp:131] Top shape: 1 16 (16)
I0607 09:57:49.378855 16098 net.cpp:139] Memory required for data: 512592
I0607 09:57:49.378859 16098 layer_factory.hpp:77] Creating layer prob
I0607 09:57:49.378865 16098 net.cpp:86] Creating Layer prob
I0607 09:57:49.378868 16098 net.cpp:408] prob <- ip2
I0607 09:57:49.378871 16098 net.cpp:382] prob -> prob
I0607 09:57:49.379010 16098 net.cpp:124] Setting up prob
I0607 09:57:49.379015 16098 net.cpp:131] Top shape: 1 16 (16)
I0607 09:57:49.379019 16098 net.cpp:139] Memory required for data: 512656
I0607 09:57:49.379020 16098 net.cpp:202] prob does not need backward computation.
I0607 09:57:49.379024 16098 net.cpp:202] ip2 does not need backward computation.
I0607 09:57:49.379025 16098 net.cpp:202] relu1 does not need backward computation.
I0607 09:57:49.379027 16098 net.cpp:202] ip1 does not need backward computation.
I0607 09:57:49.379030 16098 net.cpp:202] pool2 does not need backward computation.
I0607 09:57:49.379032 16098 net.cpp:202] conv2 does not need backward computation.
I0607 09:57:49.379035 16098 net.cpp:202] pool1 does not need backward computation.
I0607 09:57:49.379037 16098 net.cpp:202] conv1 does not need backward computation.
I0607 09:57:49.379040 16098 net.cpp:202] data does not need backward computation.
I0607 09:57:49.379041 16098 net.cpp:244] This network produces output prob
I0607 09:57:49.379047 16098 net.cpp:257] Network initialization done.
I0607 09:57:49.426604 16098 net.cpp:746] Ignoring source layer digits
I0607 09:57:49.427973 16098 net.cpp:746] Ignoring source layer loss
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/password_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/password_1.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/password_2.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/password_3.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
W0607 09:57:49.759660 16098 _caffe.cpp:135] DEPRECATION WARNING - deprecated use of Python interface
W0607 09:57:49.759683 16098 _caffe.cpp:136] Use this instead (with the named "weights" parameter):
W0607 09:57:49.759687 16098 _caffe.cpp:138] Net('/home/shuang/workspace/pycharm/trunk/resources/caffe/amountbig/billocrnet_deploy.prototxt', 1, weights='/home/shuang/workspace/pycharm/trunk/resources/caffe/amountbig/billocr_iter.caffemodel')
I0607 09:57:49.759927 16098 net.cpp:53] Initializing net from parameters: 
name: "DigitNet"
state {
  phase: TEST
  level: 0
}
layer {
  name: "data"
  type: "Input"
  top: "data"
  input_param {
    shape {
      dim: 1
      dim: 1
      dim: 42
      dim: 42
    }
  }
}
layer {
  name: "conv1"
  type: "Convolution"
  bottom: "data"
  top: "conv1"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  convolution_param {
    num_output: 64
    kernel_size: 4
    stride: 1
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "pool1"
  type: "Pooling"
  bottom: "conv1"
  top: "pool1"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  name: "conv2"
  type: "Convolution"
  bottom: "pool1"
  top: "conv2"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  convolution_param {
    num_output: 32
    kernel_size: 4
    stride: 1
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "pool2"
  type: "Pooling"
  bottom: "conv2"
  top: "pool2"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  name: "ip1"
  type: "InnerProduct"
  bottom: "pool2"
  top: "ip1"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  inner_product_param {
    num_output: 800
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "relu1"
  type: "ReLU"
  bottom: "ip1"
  top: "ip1"
}
layer {
  name: "ip2"
  type: "InnerProduct"
  bottom: "ip1"
  top: "ip2"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  inner_product_param {
    num_output: 20
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "prob"
  type: "Softmax"
  bottom: "ip2"
  top: "prob"
}
I0607 09:57:49.759968 16098 layer_factory.hpp:77] Creating layer data
I0607 09:57:49.759976 16098 net.cpp:86] Creating Layer data
I0607 09:57:49.759981 16098 net.cpp:382] data -> data
I0607 09:57:49.760001 16098 net.cpp:124] Setting up data
I0607 09:57:49.760009 16098 net.cpp:131] Top shape: 1 1 42 42 (1764)
I0607 09:57:49.760010 16098 net.cpp:139] Memory required for data: 7056
I0607 09:57:49.760015 16098 layer_factory.hpp:77] Creating layer conv1
I0607 09:57:49.760023 16098 net.cpp:86] Creating Layer conv1
I0607 09:57:49.760026 16098 net.cpp:408] conv1 <- data
I0607 09:57:49.760031 16098 net.cpp:382] conv1 -> conv1
I0607 09:57:49.761346 16098 net.cpp:124] Setting up conv1
I0607 09:57:49.761358 16098 net.cpp:131] Top shape: 1 64 39 39 (97344)
I0607 09:57:49.761360 16098 net.cpp:139] Memory required for data: 396432
I0607 09:57:49.761373 16098 layer_factory.hpp:77] Creating layer pool1
I0607 09:57:49.761380 16098 net.cpp:86] Creating Layer pool1
I0607 09:57:49.761384 16098 net.cpp:408] pool1 <- conv1
I0607 09:57:49.761389 16098 net.cpp:382] pool1 -> pool1
I0607 09:57:49.761397 16098 net.cpp:124] Setting up pool1
I0607 09:57:49.761402 16098 net.cpp:131] Top shape: 1 64 20 20 (25600)
I0607 09:57:49.761405 16098 net.cpp:139] Memory required for data: 498832
I0607 09:57:49.761407 16098 layer_factory.hpp:77] Creating layer conv2
I0607 09:57:49.761415 16098 net.cpp:86] Creating Layer conv2
I0607 09:57:49.761418 16098 net.cpp:408] conv2 <- pool1
I0607 09:57:49.761423 16098 net.cpp:382] conv2 -> conv2
I0607 09:57:49.762779 16098 net.cpp:124] Setting up conv2
I0607 09:57:49.762789 16098 net.cpp:131] Top shape: 1 32 17 17 (9248)
I0607 09:57:49.762792 16098 net.cpp:139] Memory required for data: 535824
I0607 09:57:49.762800 16098 layer_factory.hpp:77] Creating layer pool2
I0607 09:57:49.762807 16098 net.cpp:86] Creating Layer pool2
I0607 09:57:49.762810 16098 net.cpp:408] pool2 <- conv2
I0607 09:57:49.762815 16098 net.cpp:382] pool2 -> pool2
I0607 09:57:49.762823 16098 net.cpp:124] Setting up pool2
I0607 09:57:49.762828 16098 net.cpp:131] Top shape: 1 32 9 9 (2592)
I0607 09:57:49.762830 16098 net.cpp:139] Memory required for data: 546192
I0607 09:57:49.762833 16098 layer_factory.hpp:77] Creating layer ip1
I0607 09:57:49.762840 16098 net.cpp:86] Creating Layer ip1
I0607 09:57:49.762842 16098 net.cpp:408] ip1 <- pool2
I0607 09:57:49.762847 16098 net.cpp:382] ip1 -> ip1
I0607 09:57:49.777791 16098 net.cpp:124] Setting up ip1
I0607 09:57:49.777806 16098 net.cpp:131] Top shape: 1 800 (800)
I0607 09:57:49.777808 16098 net.cpp:139] Memory required for data: 549392
I0607 09:57:49.777818 16098 layer_factory.hpp:77] Creating layer relu1
I0607 09:57:49.777825 16098 net.cpp:86] Creating Layer relu1
I0607 09:57:49.777828 16098 net.cpp:408] relu1 <- ip1
I0607 09:57:49.777832 16098 net.cpp:369] relu1 -> ip1 (in-place)
I0607 09:57:49.778043 16098 net.cpp:124] Setting up relu1
I0607 09:57:49.778048 16098 net.cpp:131] Top shape: 1 800 (800)
I0607 09:57:49.778050 16098 net.cpp:139] Memory required for data: 552592
I0607 09:57:49.778053 16098 layer_factory.hpp:77] Creating layer ip2
I0607 09:57:49.778059 16098 net.cpp:86] Creating Layer ip2
I0607 09:57:49.778061 16098 net.cpp:408] ip2 <- ip1
I0607 09:57:49.778066 16098 net.cpp:382] ip2 -> ip2
I0607 09:57:49.778198 16098 net.cpp:124] Setting up ip2
I0607 09:57:49.778201 16098 net.cpp:131] Top shape: 1 20 (20)
I0607 09:57:49.778204 16098 net.cpp:139] Memory required for data: 552672
I0607 09:57:49.778208 16098 layer_factory.hpp:77] Creating layer prob
I0607 09:57:49.778214 16098 net.cpp:86] Creating Layer prob
I0607 09:57:49.778216 16098 net.cpp:408] prob <- ip2
I0607 09:57:49.778220 16098 net.cpp:382] prob -> prob
I0607 09:57:49.778367 16098 net.cpp:124] Setting up prob
I0607 09:57:49.778373 16098 net.cpp:131] Top shape: 1 20 (20)
I0607 09:57:49.778375 16098 net.cpp:139] Memory required for data: 552752
I0607 09:57:49.778378 16098 net.cpp:202] prob does not need backward computation.
I0607 09:57:49.778381 16098 net.cpp:202] ip2 does not need backward computation.
I0607 09:57:49.778383 16098 net.cpp:202] relu1 does not need backward computation.
I0607 09:57:49.778385 16098 net.cpp:202] ip1 does not need backward computation.
I0607 09:57:49.778388 16098 net.cpp:202] pool2 does not need backward computation.
I0607 09:57:49.778390 16098 net.cpp:202] conv2 does not need backward computation.
I0607 09:57:49.778393 16098 net.cpp:202] pool1 does not need backward computation.
I0607 09:57:49.778395 16098 net.cpp:202] conv1 does not need backward computation.
I0607 09:57:49.778398 16098 net.cpp:202] data does not need backward computation.
I0607 09:57:49.778400 16098 net.cpp:244] This network produces output prob
I0607 09:57:49.778408 16098 net.cpp:257] Network initialization done.
I0607 09:57:49.852059 16098 net.cpp:746] Ignoring source layer digits
I0607 09:57:49.853497 16098 net.cpp:746] Ignoring source layer loss
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/money_big_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/buyer_no_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/tax_total_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/tax_total_1.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/money_big_symbol_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/item_name_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/item_name_1.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/item_name_2.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/item_taxrate_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/item_tax_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/item_tax_1.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/item_tax_2.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/money_total_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/money_total_1.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/item_quantity_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_15/saler_bankaccount_0.jpg stdout -l chi_sim  --psm 7 --oem 2
fileName : /home/shuang/workspace/bill_ocr_work/data/zzsbj2016/2017_02_20_16_44_15.jpg 
buyer_name=北酌叼赵颐肆睹嗜[限酌蛇谷司
sh: 1: tesseract: not found
item_price=44491
saler_name=光无R明人寿保险有限公司北京分公司
saler_address=#顷t市丰台凶距三砰键$￥号豁z号蛤凉!Oc臼这扛询
buyer_bankaccount=招酮眼行北京分行世纪膝支行H0w汹硬沮饭n
money_big=ⓧ佰ⓧ仟角佰ⓧ角ⓧⓧ整
buyer_no=33O3C879S3O968G
tax_total=28481664
item_name='.其他人身保险服务
item_taxrate=￥1
item_quantity=1
saler_bankaccount=光六蛊行北京朝距支行唾窍O这O1O扔O叼玲1
saler_no=9333O3C37634OC69CR
money_small=￥3452719￥4
buyer_address=抵mssggs^日ssss寿n*aassszsszsza'aa'
item_money=4494.94
item_tax=..468.94
item_unit=
date=48时年秒3月3月秒
password=6<9+3+407/03>69-036+6695+37-++++8+/2>3<+6-42-2+5/9+3>+-245+93+2+<+3<5333<00025+30++>0302696++33+<704+<>3-2+--9<-
money_big_symbol=ⓧ
money_total=816661664
item_type=
0.0636733816009
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/saler_no_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/buyer_name_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/item_price_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/item_money_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/saler_name_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/saler_address_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/saler_address_1.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/buyer_address_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/buyer_address_1.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/buyer_bankaccount_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/buyer_bankaccount_1.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/money_small_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/money_small_1.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/date_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/password_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/password_1.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/password_2.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/password_3.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/money_big_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/buyer_no_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/tax_total_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/item_name_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/item_taxrate_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/item_tax_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/item_tax_1.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/item_tax_2.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/money_total_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/item_type_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/item_quantity_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_17_001/saler_bankaccount_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
fileName : /home/shuang/workspace/bill_ocr_work/data/zzsbj2016/2017_02_20_16_44_17_001.jpg 
buyer_name=北京亿借华辰嵌件有限责任公司
item_price=1￥￥4￥￥87
saler_name=}北京优久汇科贸有限公司
saler_address=nlu.z'ss1s1s北京市*sgn争咸甫azs口sa下-昼cws
buyer_bankaccount=11o9Oz4aszlOzol招商银行北京分行世铝城支行
money_big=角ⓧ角仟ⓧ佰角角角角
buyer_no=33O3OH79S3O9G82
tax_total=383817.
item_name=腰务费
item_taxrate=￥4
item_quantity=1
saler_bankaccount=中借银行北京中关村支行7口121O182zO0O544l5
saler_no=3303O8803387743
money_small=934448189
buyer_address="t"-sa&sm*sg重4ogsssw*ssnag画s-*i@ase~*
item_money=4484344
item_tax=..84844
item_unit=
date=时时年时月时日
password=-4>/*3*65+*<--373//560+-4>762<*492>326-/*-5+/<3<44->63/<365/<*>>673>95028//33<4095593532+/*-3+/63<40+760749*
money_big_symbol=
money_total=942842.42
item_type=.
0.0674155901271
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/saler_no_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/buyer_name_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/item_money_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/saler_name_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/saler_address_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/saler_address_1.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/buyer_address_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/buyer_bankaccount_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/buyer_bankaccount_1.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/money_small_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/date_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/password_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/password_1.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/password_2.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/password_3.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/money_big_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/money_big_1.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/buyer_no_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/tax_total_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/tax_total_1.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/money_big_symbol_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/item_name_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/item_name_1.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/item_taxrate_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/item_tax_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/money_total_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/saler_bankaccount_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_18/saler_bankaccount_1.jpg stdout -l chi_sim  --psm 7 --oem 2
fileName : /home/shuang/workspace/bill_ocr_work/data/zzsbj2016/2017_02_20_16_44_18.jpg 
buyer_name={b京石估半辰故祥有谅贡估公司
sh: 1: tesseract: not found
item_price=
saler_name=北京市东升靳炉厂
saler_address=--北京市海淀区演河小章路后屯衬东斑n晒迫z起
buyer_bankaccount=11OO冰冲江OOl招商锯行北京分行世纪城支行
money_big=万万角角玖整整
buyer_no=IIOIO87953O9682
tax_total=8349869
item_name=.-租盒
item_taxrate=444
item_quantity=
saler_bankaccount=.北京农商行负升支钎4w邓1皿w)哑z汀
saler_no=9II3OIO8IO39O3524C
money_small=￥￥8￥969
buyer_address=袒梗畔谭酗曰@袒s哼田嗣峰蛔靶哮屿诵皿窒m*一一m
item_money=9￥￥.84
item_tax=498.84
item_unit=
date=4847年83月38日
password=<529><052<03+<>/95-4479+30/*-9/39-836>/-7+>577-+*<3**+0>>>>09895-/<0-81-99339925293-3593/<9+3<<2>2
money_big_symbol=ⓧ
money_total=486996.09
item_type=
0.0638941955603
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/saler_no_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/buyer_name_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/item_price_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/item_money_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/saler_name_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/saler_address_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/saler_address_1.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/buyer_address_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/buyer_address_1.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/buyer_address_2.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/buyer_bankaccount_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/buyer_bankaccount_1.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/money_small_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/date_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/password_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/password_1.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/password_2.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/password_3.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/money_big_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/buyer_no_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/tax_total_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/item_name_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/item_taxrate_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/item_tax_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/item_tax_1.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/item_tax_2.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/item_tax_3.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/item_tax_4.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/money_total_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/item_unit_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/saler_bankaccount_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_13/saler_bankaccount_1.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
fileName : /home/shuang/workspace/bill_ocr_work/data/zzsbj2016/2017_02_20_16_44_13.jpg 
buyer_name=北京亿借华辰软件有限责任公司
item_price=.
saler_name=北京华字倍蛊技术有限公司
saler_address=cza@z@a,zsm'1b*m@ggw*##m1g@畔{sagcau'
buyer_bankaccount=1lO9Oz496zlOzOl招商银行北京分行世纪城支行
money_big=角角玖角角
buyer_no=33O3O87933C968W
tax_total=￥34248175
item_name=服务费
item_taxrate=￥1
item_quantity=
saler_bankaccount=1lO9O663911O8O1招意银行北京分行演华园支行
saler_no=3303O8695O38OSY
money_small=4488888188
buyer_address=vsssss"ts.s*抵gmsgg重^nmsm,s*s*nagmea'@ag*wzt
item_money=18879￥.
item_tax=￥...￥...44￥8￥1
item_unit=论
date=时时年83月时日
password=-<68/-7++<9/4>432004*0336099-56*22759643<79//>5*+6*/3>*49++9->0-332244+235>3/6>29/<9929253<7*//97<<69*3/-+69
money_big_symbol=
money_total=448887945
item_type=
0.0676985080982
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/saler_no_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/buyer_name_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_price_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_price_1.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_price_2.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_price_3.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_price_4.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_money_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_money_1.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_money_2.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_money_3.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_money_4.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/saler_name_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/saler_address_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/saler_address_1.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/saler_address_2.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/buyer_address_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/buyer_address_1.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/buyer_address_2.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/buyer_bankaccount_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/buyer_bankaccount_1.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/money_small_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/money_small_1.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/date_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/password_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/password_1.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/password_2.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/password_3.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/money_big_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/buyer_no_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/tax_total_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_name_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_name_1.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_name_2.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_name_3.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_name_4.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_name_5.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_name_6.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_name_7.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_name_8.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_name_9.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_taxrate_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_taxrate_1.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_taxrate_2.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_taxrate_3.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_taxrate_4.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_tax_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_tax_1.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_tax_2.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_tax_3.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_tax_4.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_tax_5.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_tax_6.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_tax_7.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/money_total_0.jpg stdout -l eng+chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_type_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_type_1.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_type_2.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_type_3.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_type_4.jpg stdout -l chi_sim  --psm 7 --oem 2
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_unit_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_unit_1.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_unit_2.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_unit_3.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_quantity_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_quantity_1.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_quantity_2.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_quantity_3.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/item_quantity_4.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/saler_bankaccount_0.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
tesseract /home/shuang/workspace/bill_ocr_work/data/zzsbj2016_out/images/2017_02_20_16_44_12/saler_bankaccount_1.jpg stdout -l chi_sim  --psm 7 --oem 2
sh: 1: tesseract: not found
fileName : /home/shuang/workspace/bill_ocr_work/data/zzsbj2016/2017_02_20_16_44_12.jpg 
buyer_name=北京亿信华辰软件有限责任公司
item_price=￥9￥1941￥￥48449￥844￥￥4￥￥￥48￥8.￥￥￥44￥￥9.4￥￥4
saler_name=北京华宇信患技术育罩公司
saler_address=sa}asssczaz'砒*m@ggw*#*gts@e'@aF~wu
buyer_bankaccount=11O9Oz49句}1O2Ol招雨银行北京分行世织矮支行
money_big=捌角捌佰ⓧ仟玖整
buyer_no=33O3O87953O9682
tax_total=4448725184
item_name=eSi助t企业运维系绕S770O智皑睹由交换机皿2m-S4高蜡业务蹄由器OceenStsrSNS2224光纤交换机比}55000ceen3tpr
item_taxrate=4￥14￥11￥14￥14￥1
item_quantity=12242
saler_bankaccount=11O9O663911O801招商银行北京分行演华园支行
saler_no=I3O3O869SO38O5M
money_small=￥88804966
buyer_address=swmss"1w.sz&*wsgg重^日gse's*#*aaaaeassag*w,辜
item_money=444949109994449939449￥9.9149￥49￥
item_tax=481￥914￥.9743￥8￥..￥￥444494￥14￥.
item_unit=0套委奎
date=时时年时月时日
password=7<>6737*9-33<*783>90736+7<*-523-02>*99**3993<<<<>99/836<9*9933+9293//0334*<6995/++*9389//*39*3<9**-9**937+>2
money_big_symbol=
money_total=￥737484.44
item_type=L,-.|j,

Process finished with exit code 0
