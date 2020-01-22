from tf_keras_1.losses.imports import *
from system.imports import *


@accepts(dict, weight=[list, type(np.array([1, 2, 3])), float, type(None)], batch_axis=int, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def l1(system_dict, weight=None, batch_axis=0):
    system_dict["local"]["criterion"] = "l1";
    system_dict["hyper-parameters"]["loss"]["name"] = "l1";
    system_dict["hyper-parameters"]["loss"]["params"]["weight"] = weight;
    system_dict["hyper-parameters"]["loss"]["params"]["batch_axis"] = batch_axis;
    system_dict["hyper-parameters"]["status"] = True;
    return system_dict;


@accepts(dict, weight=[list, type(np.array([1, 2, 3])), float, type(None)], batch_axis=int, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def l2(system_dict, weight=1.0, batch_axis=0):
    system_dict["local"]["criterion"] = "l2";
    system_dict["hyper-parameters"]["loss"]["name"] = "l2";
    system_dict["hyper-parameters"]["loss"]["params"]["weight"] = weight;
    system_dict["hyper-parameters"]["loss"]["params"]["batch_axis"] = batch_axis;
    system_dict["hyper-parameters"]["status"] = True;
    return system_dict;


@accepts(dict, weight=[list, type(np.array([1, 2, 3])), float, type(None)], batch_axis=int, 
    axis_to_sum_over=int, label_as_categories=bool, label_smoothing=bool, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def crossentropy(system_dict, weight=None, batch_axis=0, axis_to_sum_over=-1, 
    label_as_categories=True, label_smoothing=False):
    system_dict["local"]["criterion"] = "crossentropy";
    system_dict["hyper-parameters"]["loss"]["name"] = "crossentropy";
    system_dict["hyper-parameters"]["loss"]["params"]["weight"] = weight;
    system_dict["hyper-parameters"]["loss"]["params"]["batch_axis"] = batch_axis;
    system_dict["hyper-parameters"]["loss"]["params"]["axis_to_sum_over"] = axis_to_sum_over;
    system_dict["hyper-parameters"]["loss"]["params"]["label_as_categories"] = label_as_categories;
    system_dict["hyper-parameters"]["loss"]["params"]["label_smoothing"] = label_smoothing;
    system_dict["hyper-parameters"]["status"] = True;
    return system_dict;



@accepts(dict, weight=[list, type(np.array([1, 2, 3])), float, type(None)], batch_axis=int, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def binary_crossentropy(system_dict, weight=None, batch_axis=0):
    system_dict["local"]["criterion"] = "binarycrossentropy";
    system_dict["hyper-parameters"]["loss"]["name"] = "binarycrossentropy";
    system_dict["hyper-parameters"]["loss"]["params"]["weight"] = weight;
    system_dict["hyper-parameters"]["loss"]["params"]["batch_axis"] = batch_axis;
    system_dict["hyper-parameters"]["status"] = True;
    return system_dict;


@accepts(dict, log_pre_applied=bool, weight=[list, type(np.array([1, 2, 3])), float, type(None)], batch_axis=int, 
    axis_to_sum_over=int, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def kldiv(system_dict, log_pre_applied=False, weight=None, batch_axis=0, axis_to_sum_over=-1):
    system_dict["local"]["criterion"] = "kldiv";
    system_dict["hyper-parameters"]["loss"]["name"] = "kldiv";
    system_dict["hyper-parameters"]["loss"]["params"]["log_pre_applied"] = log_pre_applied;
    system_dict["hyper-parameters"]["loss"]["params"]["weight"] = weight;
    system_dict["hyper-parameters"]["loss"]["params"]["batch_axis"] = batch_axis;
    system_dict["hyper-parameters"]["loss"]["params"]["axis_to_sum_over"] = axis_to_sum_over;
    system_dict["hyper-parameters"]["status"] = True;
    return system_dict;


@accepts(dict, weight=[list, type(np.array([1, 2, 3])), float, type(None)], batch_axis=int, margin=int, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def hinge(system_dict, weight=None, batch_axis=0, margin=1):
    system_dict["local"]["criterion"] = "hinge";
    system_dict["hyper-parameters"]["loss"]["name"] = "hinge";
    system_dict["hyper-parameters"]["loss"]["params"]["margin"] = margin;
    system_dict["hyper-parameters"]["loss"]["params"]["weight"] = weight;
    system_dict["hyper-parameters"]["loss"]["params"]["batch_axis"] = batch_axis;
    system_dict["hyper-parameters"]["status"] = True;
    return system_dict;


@accepts(dict, weight=[list, type(np.array([1, 2, 3])), float, type(None)], batch_axis=int, margin=int, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def squared_hinge(system_dict, weight=None, batch_axis=0, margin=1):
    system_dict["local"]["criterion"] = "squaredhinge";
    system_dict["hyper-parameters"]["loss"]["name"] = "squaredhinge";
    system_dict["hyper-parameters"]["loss"]["params"]["margin"] = margin;
    system_dict["hyper-parameters"]["loss"]["params"]["weight"] = weight;
    system_dict["hyper-parameters"]["loss"]["params"]["batch_axis"] = batch_axis;
    system_dict["hyper-parameters"]["status"] = True;
    return system_dict;






'''
@accepts(dict, weight=[list, type(np.array([1, 2, 3])), float, type(None)], size_average=[list, type(np.array([1, 2, 3])), float, type(None)], 
    ignore_index=int, reduction=str, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def categorical_crossentropy(system_dict, weight=None, size_average=None, ignore_index=-100, reduction='mean'):
    system_dict["local"]["criterion"] = "categoricalcrossentropy";
    system_dict["hyper-parameters"]["loss"]["name"] = "categoricalcrossentropy";
    system_dict["hyper-parameters"]["loss"]["params"]["weight"] = weight;
    system_dict["hyper-parameters"]["loss"]["params"]["size_average"] = size_average;
    system_dict["hyper-parameters"]["loss"]["params"]["ignore_index"] = ignore_index;
    system_dict["hyper-parameters"]["loss"]["params"]["reduce"] = None;
    system_dict["hyper-parameters"]["loss"]["params"]["reduction"] = reduction;
    system_dict["hyper-parameters"]["status"] = True;
    return system_dict;




@accepts(dict, weight=[list, type(np.array([1, 2, 3])), float, type(None)], size_average=[list, type(np.array([1, 2, 3])), float, type(None)], 
    ignore_index=int, reduction=str, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def sparse_categorical_crossentropy(system_dict, weight=None, size_average=None, ignore_index=-100, reduction='mean'):
    system_dict["local"]["criterion"] = "sparsecategoricalcrossentropy";
    system_dict["hyper-parameters"]["loss"]["name"] = "sparsecategoricalcrossentropy";
    system_dict["hyper-parameters"]["loss"]["params"]["weight"] = weight;
    system_dict["hyper-parameters"]["loss"]["params"]["size_average"] = size_average;
    system_dict["hyper-parameters"]["loss"]["params"]["ignore_index"] = ignore_index;
    system_dict["hyper-parameters"]["loss"]["params"]["reduce"] = None;
    system_dict["hyper-parameters"]["loss"]["params"]["reduction"] = reduction;
    system_dict["hyper-parameters"]["status"] = True;
    return system_dict;





@accepts(dict, weight=[list, type(np.array([1, 2, 3])), float, type(None)], size_average=[list, type(np.array([1, 2, 3])), float, type(None)], 
    ignore_index=int, reduction=str, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def categorical_hinge(system_dict, weight=None, size_average=None, ignore_index=-100, reduction='mean'):
    system_dict["local"]["criterion"] = "categoricalhinge";
    system_dict["hyper-parameters"]["loss"]["name"] = "categoricalhinge";
    system_dict["hyper-parameters"]["loss"]["params"]["weight"] = weight;
    system_dict["hyper-parameters"]["loss"]["params"]["size_average"] = size_average;
    system_dict["hyper-parameters"]["loss"]["params"]["ignore_index"] = ignore_index;
    system_dict["hyper-parameters"]["loss"]["params"]["reduce"] = None;
    system_dict["hyper-parameters"]["loss"]["params"]["reduction"] = reduction;
    system_dict["hyper-parameters"]["status"] = True;
    return system_dict;





@accepts(dict, weight=[list, type(np.array([1, 2, 3])), float, type(None)], size_average=[list, type(np.array([1, 2, 3])), float, type(None)], 
    reduce=type(None), reduction=str, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def binary_crossentropy(system_dict, weight=None, size_average=None, reduce=None, reduction='mean'):
    system_dict["local"]["criterion"] = "binarycrossentropy";
    system_dict["hyper-parameters"]["loss"]["name"] = "binarycrossentropy";
    system_dict["hyper-parameters"]["loss"]["params"]["weight"] = weight;
    system_dict["hyper-parameters"]["loss"]["params"]["size_average"] = size_average;
    system_dict["hyper-parameters"]["loss"]["params"]["reduce"] = reduce;
    system_dict["hyper-parameters"]["loss"]["params"]["reduction"] = reduction;
    system_dict["hyper-parameters"]["status"] = True;
    return system_dict;
'''