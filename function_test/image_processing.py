import json
import time
import datetime
import os,glob
import sys
import numpy as np
import matplotlib.pyplot as plt

def mk2DArray(self):
    """
       Creates a 2D array from raw json.
    """
    len_acquisition = len(self.tmp)
    img = []
    tmpline = []
    lineindex = 0

    for k in range(len_acquisition):
        if self.IDLine[k] != lineindex:
            img.append(tmpline)
            lineindex = self.IDLine[k]
            tmpline = []
        else:
            tmpline.append(self.tmp[k])

    duration_self = int(float(self.f) * self.Duration)

    y = [s for s in img if (len(s) > duration_self - 10 and len(s) < duration_self + 10)]
    if self.Nacq > 1:
        clean_image = np.zeros((len(y), len(self.tmp) / len(y)))
    else:
        clean_image = np.zeros((len(y), 1))

    for i in range(len(y)):
        clean_image[i][0:len(y[i])] = y[i]

    img_size = np.shape(clean_image)
    str(float(self.f)*Duration)
    Duration = (self.parameters['LengthAcq'] - self.parameters['DeltaAcq']) / 1000.0

    clean_image = clean_image[:, :int(Duration * self.f)]
    plt.figure(figsize=(15, 10))
    if self.Nacq > 1:
        print(img_size[1], img_size[0])
        plt.imshow(np.sqrt(np.abs(clean_image)), cmap='gray', aspect=0.5 * (img_size[1] / img_size[0]),
                   interpolation='nearest')
    else:
        plt.plot(self.t[0:self.len_line], self.tmp[0:self.len_line], 'b-')
        # plt.show()

    plt.title(self.create_title_text())
    plt.tight_layout()
    file_name = "images/2DArray_" + self.iD + "-" + str(self.N) + ".jpg"
    plt.savefig(file_name)
    plt.show()
    self.raw_2d_image = clean_image  # @todo: reuse this 2D image ?

    return clean_image

def plot_detail(self, nb_line, Start, Stop):  # @todo: use it when processing data
    """
       Shows and displays a given line, with start and stop boundaries.
    """
    # TLine = self.len_line/self.f #@unused
    Offset = nb_line * self.len_line

    plot_time_series = self.t[Offset + int(Start / self.f):Offset + int(Stop * self.f)]
    plot_signal = self.tmp[Offset + int(Start / self.f):int(Stop * self.f)]
    # @todo .. what happens if no EnvHil ?
    plot_enveloppe = self.EnvHil[Offset + int(Start / self.f):int(Stop * self.f)]

    plot_title = "Detail of " + self.iD + " - acq. #: " + str(self.N) + ", between "
    plot_title += str(Start) + " and " + str(Stop) + " (line #" + str(nb_line) + ")."

    plt.figure(figsize=(15, 5))
    plt.plot(plot_time_series, plot_signal, 'b-')
    plt.plot(plot_time_series, plot_enveloppe, 'y-')
    plt.title(plot_title)
    plt.xlabel('Time in us')
    plt.tight_layout()

    file_name = "images/detail_" + self.iD + "-" + str(self.N) + "-"
    file_name += str(Start) + "-" + str(Stop) + "-line" + str(nb_line) + ".jpg"
    plt.savefig(file_name)
    plt.show()


def mkFiltered(self, original_image):
    """
       Takes the image, then filters it around self.fPiezo .
    """
    filtered_image = []
    fft_image_filtered = []
    if len(original_image):
        num_lines, length_lines = np.shape(original_image)
        f_array = [X * self.f / length_lines for X in range(length_lines)]
        for k in range(num_lines):  # number of images
            fft_single_line = np.fft.fft(original_image[k])
            fft_image_filtered.append(fft_single_line)
            for p in range(len(fft_single_line) / 2 + 1):
                f_min = (1000.0 * self.fPiezo * 0.7)
                f_max = (1000.0 * self.fPiezo * 1.27)
                if (f_array[p] > f_max or f_array[p] < f_min):
                    fft_single_line[p] = 0
                    fft_single_line[-p] = 0
            filtered_image.append(np.real(np.fft.ifft(fft_single_line)))
    return filtered_image, fft_image_filtered


def mkSpectrum(self, img):
    """
       Creates a 2D array spectrum from 2D image.
    """
    Spectrum = []
    # Filtered = [] #@unused
    if len(img):
        n_lines, len_lines = np.shape(img)
        self.FFT_x = [X * self.f / len_lines for X in range(len_lines)]  # @usuned, why?
        for k in range(n_lines):
            fft_single_line = np.fft.fft(img[k])
            Spectrum.append(fft_single_line[0:n_lines / 2])

        plt.figure(figsize=(15, 10))
        plt.imshow(np.sqrt(np.abs(Spectrum)), extent=[0, 1000.0 * self.f / 2, n_lines, 0], cmap='hsv', aspect=30.0,
                   interpolation='nearest')

        plt.axvline(x=(1000 * self.fPiezo * 1.27), linewidth=4, color='b')
        plt.axvline(x=(1000 * self.fPiezo * 0.7), linewidth=4, color='b')

        plt.xlabel("Frequency (kHz)")
        plt.ylabel("Lines #")

        plt.title(self.create_title_text())
        plt.tight_layout()

        file_name = "images/Spectrum_" + self.iD + "-" + str(self.N) + ".jpg"
        plt.savefig(file_name)
    else:
        print("2D Array not created yet")

    return np.abs(Spectrum)