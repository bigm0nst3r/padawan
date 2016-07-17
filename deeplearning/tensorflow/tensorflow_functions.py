__author__ = "Sreejith Sreekumar <sreejith.sreekumar@247-inc.com>"


def softmax_cross_entropy_with_logits(logits, labels, name=None):
  """Computes softmax cross entropy between `logits` and `labels`.

  Measures the probability error in discrete classification tasks in which the
  classes are mutually exclusive (each entry is in exactly one class).  For
  example, each CIFAR-10 image is labeled with one and only one label: an image
  can be a dog or a truck, but not both.

  **NOTE:**  While the classes are mutually exclusive, their probabilities
  need not be.  All that is required is that each row of `labels` is
  a valid probability distribution.  If they are not, the computation of the
  gradient will be incorrect.

  If using exclusive `labels` (wherein one and only
  one class is true at a time), see `sparse_softmax_cross_entropy_with_logits`.

  **WARNING:** This op expects unscaled logits, since it performs a `softmax`
  on `logits` internally for efficiency.  Do not call this op with the
  output of `softmax`, as it will produce incorrect results.

  `logits` and `labels` must have the same shape `[batch_size, num_classes]`
  and the same dtype (either `float32` or `float64`).

  Args:
    logits: Unscaled log probabilities.
    labels: Each row `labels[i]` must be a valid probability distribution.
    name: A name for the operation (optional).

  Returns:
    A 1-D `Tensor` of length `batch_size` of the same type as `logits` with the
    softmax cross entropy loss.
  """
  # TODO(pcmurray) Raise an error when the labels do not sum to 1. Note: This
  # could break users who call this with bad labels, but disregard the bad
  # results.

  # The second output tensor contains the gradients.  We use it in
  # _CrossEntropyGrad() in nn_grad but not here.
  cost, unused_backprop = gen_nn_ops._softmax_cross_entropy_with_logits(
      logits, labels, name=name)
  return cost






def reduce_mean(input_tensor, reduction_indices=None, keep_dims=False,
                name=None):
  """Computes the mean of elements across dimensions of a tensor.

  Reduces `input_tensor` along the dimensions given in `reduction_indices`.
  Unless `keep_dims` is true, the rank of the tensor is reduced by 1 for each
  entry in `reduction_indices`. If `keep_dims` is true, the reduced dimensions
  are retained with length 1.

  If `reduction_indices` has no entries, all dimensions are reduced, and a
  tensor with a single element is returned.

  For example:

  ```python
  # 'x' is [[1., 1.]
  #         [2., 2.]]
  tf.reduce_mean(x) ==> 1.5
  tf.reduce_mean(x, 0) ==> [1.5, 1.5]
  tf.reduce_mean(x, 1) ==> [1.,  2.]
  ```

  Args:
    input_tensor: The tensor to reduce. Should have numeric type.
    reduction_indices: The dimensions to reduce. If `None` (the default),
      reduces all dimensions.
    keep_dims: If true, retains reduced dimensions with length 1.
    name: A name for the operation (optional).

  Returns:
    The reduced tensor.
  """
  return gen_math_ops._mean(input_tensor, _ReductionDims(input_tensor,
                                                         reduction_indices),
                            keep_dims, name=name)
  



