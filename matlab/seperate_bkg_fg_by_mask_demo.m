% Seperate foreground image and background image by mask image

clear, clc;
img = imread('./Lenna.jpeg');
mask_img = imread('./mask.jpeg');

figure;
subplot(1, 4, 1)
imshow(img, []);
title('original image')
subplot(1, 4, 2)
imshow(mask_img, []);
title('mask image');

mask = uint8(im2bw(mask_img, 0.5)); % set threhold between 0 and 1

r_img = img(:, :, 1); % red channel
g_img = img(:, :, 2); % green channel
b_img = img(:, :, 3); % blue channel

% get foreground image
fore_img(:, :, 1) = r_img.*mask;
fore_img(:, :, 2) = g_img.*mask;
fore_img(:, :, 3) = b_img.*mask;
subplot(1, 4, 3);
imshow(fore_img, []);
title('foreground image');

% get background image
back_img = img - fore_img;
subplot(1, 4, 4);
imshow(back_img, []);
title('background image');
