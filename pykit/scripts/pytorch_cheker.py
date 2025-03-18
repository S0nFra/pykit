if __name__ == "__main__":
    import torch

    print("PyTorch",torch.__version__)
    print("CUDA availabe:",torch.cuda.is_available())
    print("CUDA Device count:",torch.cuda.device_count())
    print("CUDA current device:",torch.cuda.current_device())

    dev = input("Insert device index for details (-1 to exit): ")

    if int(dev) > -1:
        print("Device link:",torch.cuda.device(0))
        print("Device name:",torch.cuda.get_device_name(0))
