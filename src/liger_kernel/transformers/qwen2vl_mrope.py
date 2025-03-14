from liger_kernel.ops.qwen2vl_mrope import LigerQwen2VLMRopeFunction


def liger_multimodal_rotary_pos_emb(q, k, cos, sin, mrope_section, unsqueeze_dim=1):
    """
    Applies Multimodal Rotary Positional Embedding (M-RoPE) operation to query and key states.

    Args:
        q (torch.Tensor): The query tensor of shape (bsz, n_q_head, seq_len, head_dim).
        k (torch.Tensor): The key tensor of shape (bsz, n_kv_head, seq_len, head_dim).
        cos (torch.Tensor): The cosine tensor of shape (3, bsz, seq_len, head_dim).
        sin (torch.Tensor): The sine tensor of shape (3, bsz, seq_len, head_dim).
        mrope_section (List[int]): The multimodal rope section for channel dimension of temporal, height and width in rope calculation.
        unsqueeze_dim (int, optional): The dimension to unsqueeze. Defaults to 1.

    Returns:
        Tuple[torch.Tensor, torch.Tensor]: The query and key tensors after applying the M-RoPE operation.
    """

    return LigerQwen2VLMRopeFunction.apply(q, k, cos, sin, mrope_section, unsqueeze_dim)
