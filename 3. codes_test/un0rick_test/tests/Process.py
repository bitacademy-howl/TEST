import logging
import sys

class Process:

    def detect(data, axis=-1):
        """
        perform envelope detection on input data by calculating the magnitude of
        the analytic signal

        :param data: input data to envelope detect
        :param axis: dimension along which detection is performed, default: -1. Basic
        :return: env_data (np.array)
        """
        from scipy.signal import hilbert
        import numpy as np

        data = np.array(data)

        analytic_data = hilbert(data, N=None, axis=axis)
        env_data = np.absolute(analytic_data)

        msg = '[detect] Envelope detection finished.'
        print(msg)
        logging.debug(msg)

        return env_data

    def log_compress(env_image):
        """
        Log compression of envelope detected US image

        :param env_image: numpy array of envelope detected
         US data
        :return: numpy array of log compressed US image
        """
        import sys
        import numpy as np
        import logging

        img_type = type(env_image).__module__
        if img_type != np.__name__:
            msg = 'ERROR [log_compress] input is not numpy array. ' \
                  'Exiting script...'
            print(msg)
            logging.error(msg)
            sys.exit()

        scaled_image = env_image/env_image.max()
        log_image = 20*np.log10(scaled_image)

        msg = '[log_compress] Log compression finished.'
        print(msg)
        logging.debug(msg)

        return log_image

    def reshape_rf(rf_vector, axial_samples, num_beams):
        """
        read in 1. Basic-d vector of rf data and shape into 2. modules-d image based on number
        of axial samples and number of transmit beams

        :param rf_vector: 1. Basic-d float array of rf data read from binary
        :param axial_samples: number of samples in axial dimension
        :param num_beams: number of transmit beams
        :return: matrix (np.array [num_beams][axial_samples])
        """
        import numpy as np

        rf_vector = np.array(rf_vector)
        rf_vector = rf_vector.squeeze()

        if rf_vector.ndim > 1:
            msg = 'ERROR [reshape_rf] Vector input is not 1. Basic-d. Exiting script...'
            print(msg)
            logging.error(msg)
            sys.exit()

        try:
            matrix = np.reshape(rf_vector, (num_beams, axial_samples))
            msg = '[reshape_rf] Data reshaping finished (beam x axial sample).'
            print(msg)
            logging.debug(msg)
        except ValueError as err:
            if rf_vector.size != axial_samples * num_beams:
                msg = 'ERROR [reshape_rf] Mismatch in vector length and image ' \
                      'dimensions: {0}. Exiting script...'.format(err)
                print(msg)
                logging.error(msg)
                sys.exit()

        return matrix

    def apply_tgc(data, dz, adb=0.5):
        """
        perform time gain compensation to compensate for loss due to exponential
        decay in signal with depth

        :param data: input matrix
        :param dz: axial sample increment
        :param adb: attenuation coefficient db, default: 0.5
        :return: data_tgc (np.array)
        """
        import numpy as np
        np_per_db = 1/(20*np.log10(np.exp(1)))

        z_array = dz*np.array([ii for ii in range(0, data.shape[1])])

        data_tgc = data
        for beam in range(0, data.shape[0]):
            data_tgc[beam] = np.multiply(data[beam], np.exp(np_per_db*adb*z_array))

        msg = '[apply_tgc] Exponential TGC applied with a=%.2f db.' %\
              adb
        logging.info(msg)
        print(msg)

        return data_tgc