import numpy as np

def depthwise_convolution(image, kernel):
    h, w, c = image.shape
    kh, kw, c = kernel.shape

    pad_image = np.pad(image, ((kh//2, kh//2), (kw//2, kw//2), (0, 0)), mode='constant')

    output = np.zeros((h, w, c))

    # Perform depthwise convolution
    for i in range(h):
        for j in range(w):
            for k in range(c):
                output[i, j, k] = np.sum(pad_image[i:i+kh, j:j+kw, k] * kernel[:,:,k])

    return output

def pointwise_convolution(image, kernel):
    # Perform pointwise convolution
    return np.sum(image * kernel, axis=2)

def main():
    # Example input image and kernel
    image = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                      [[9, 8, 7], [6, 5, 4], [3, 2, 1]],
                      [[2, 4, 6], [8, 1, 3], [5, 7, 9]]])
    kernel = np.array([[[1, 0, -1], [1, 0, -1], [1, 0, -1]],
                       [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]],
                       [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]])

    # External flag to indicate the type of convolution (depthwise or pointwise)
    convolution_type = input("Enter 'depthwise' or 'pointwise' for convolution: ")

    if convolution_type == 'depthwise':
       
        convoluted_image = depthwise_convolution(image, kernel)
    elif convolution_type == 'pointwise':
    
        convoluted_image = pointwise_convolution(image, kernel)
    else:
        print("Invalid convolution type. Please enter 'depthwise' or 'pointwise'.")
        return

    print("Convoluted Image:")
    print(convoluted_image)

if __name__ == "__main__":
    main()
