import torch
import torch.nn.quantized.functional

class Dropout(torch.nn.Dropout):
    r"""This is the quantized equivalent of :class:`~torch.nn.Dropout`.
        And this is a placeholder to enable models where fp32 tensors
        had dropout to work with quantized tensors in train and eval mode.

    Args:
        p: probability of an element to be zeroed
        inplace: can optionally do the operation in-place. Default: ``False``
    """

    def forward(self, input):
        return input

    def _get_name(self):
        return 'QuantizedDropout'

    @staticmethod
    def from_float(mod):
        return Dropout(mod.p, mod.inplace)
